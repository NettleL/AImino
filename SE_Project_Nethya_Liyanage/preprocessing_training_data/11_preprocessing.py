import os
import numpy as np
import torch
from Bio import SeqIO
import time
import gc

# PREPROCESSING FUNCTIONS

def load_fasta(file_path):
    """
    Reads FASTA file using Biopython and returns a dictionary mapping each protein ID to its sequence
    """
    fasta_dict = {}
    
    # SeqIO.parse returns an iterator where each record contains an ID and a sequence.
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_dict[record.id] = str(record.seq)
    print(f"Loaded {len(fasta_dict)} sequences from the FASTA file")
    return fasta_dict

def one_hot_encode(sequence):
    """
    Converts protein sequence into one-hot encoded numpy array with output shape (L, number_of_amino_acids) (where L = sequence length)
    """
    
    # Defines the amino acid dictionary: 20 amino acids plus 'X' for unknown
    aa = "ACDEFGHIKLMNPQRSTVWYX"
    aa_dict = {}
    for index_num in range(21):
        amino_acid = aa[index_num]
        aa_dict[amino_acid] = index_num

    L = len(sequence)
    d = 21 
    encoding = np.zeros((L, d), dtype=np.float16)
    for i, amino_acid in enumerate(sequence):
        aa_index = aa_dict.get(amino_acid, aa_dict.get("X"))
        encoding[i, aa_index] = 1.0
    return encoding


def one_hot_encode_dssp3(dssp3):
    """
    One hot encodes dssp3 into (L, 3) format
    """
    L = len(dssp3)
    d = 3
    encoding = np.zeros((L, d), dtype=np.float16)
    
    for i, label in enumerate(dssp3):
        label = int(label)
        if label in [0, 1, 2]: 
            encoding[i, label] = 1.0
        else:
            encoding[i, :] = [0, 0, 0]
    
    return encoding
    

def min_max_normalize(array):
    """
    Normalizes numpy array using min-max scaling
    """
    array_min = np.min(array)
    array_max = np.max(array)
    if array_max - array_min > 0:
        normalized = (array - array_min) / (array_max - array_min)
    else:
        normalized = array
    return normalized.astype(np.float16)

def process_npz(npz_file):
    """
    Loads NPZ file and processes the arrays:
      - Reshapes phi, psi arrays to (L, 1) if needed
      - Normalizes phi, psi, dist_ca using min_max_normalise()
      - Converts dssp3 to one hot encoding 
    """
    data = np.load(npz_file)
    
    dssp3 = data["dssp3"].astype(np.float16)
    phi = data["phi"].astype(np.float16)
    psi = data["psi"].astype(np.float16)
    mask1d = data["mask1d"].astype(np.float16)
    dist_ca = data["dist_ca"].astype(np.float16)
    msa = data["msa"].astype(np.float16)

    
    # to ensure per-residue arrays (dssp3, phi, psi) have shape (L, 1)
    if phi.ndim == 1:
        phi = phi.reshape(-1, 1)
    if psi.ndim == 1:
        psi = psi.reshape(-1, 1)
    
    # normalise phi, psi & dist_ca
    phi = min_max_normalize(phi)
    psi = min_max_normalize(psi)
    dist_ca = min_max_normalize(dist_ca)
    
    dssp3 = one_hot_encode_dssp3(dssp3)
    
    # msa needs to be transposed - msa.shape = (Rows, Length) but needs to be (Length, Rows)
    msa = msa.T
    
    features = {
        "dssp3": dssp3,
        "phi": phi,
        "psi": psi,
        "msa": msa,
        "dist_ca": dist_ca,
        "mask1d": mask1d
    }
    
    # kept mask1d for future confidence metric
    return features

def create_sequential_features(one_hot, dssp3, phi, psi, msa, mask1d):
    """
    Combines per-residue features into a sequential representation suitable for an RNN
    
    Process
    - concatenates the per-residue features (one-hot encoded sequence, one-hot encoded dssp3, phi, psi, msa)
      to form an array of shape (L, F) (F = total no. of per-residue features)
    - Returns array with shape (L, F)
    """
    
    L = one_hot.shape[0]
    
    fixed_msa_dim = 400 # despite average being approx 6100 - easier computationally
    
    # Adjust msa dimensions: current shape is (L, msa_dim)
    current_msa_dim = msa.shape[1]
    if current_msa_dim > fixed_msa_dim:
        msa_fixed = msa[:, :fixed_msa_dim]
    elif current_msa_dim < fixed_msa_dim:
        # Pad with zeros along the feature dimension.
        pad_width = fixed_msa_dim - current_msa_dim
        msa_fixed = np.pad(msa, ((0, 0), (0, pad_width)), mode='constant', constant_values=0)
    else:
        msa_fixed = msa
    
    sequential_features = np.concatenate([one_hot, dssp3, phi, psi, msa_fixed, mask1d.reshape(-1, 1)], axis=1)

    return sequential_features
    
# BATCH PROCESSING

def process_batch(fasta_dict, npz_folder, batch_keys): # Batch processing is relic from when trying to reduce memory usage for CNN (not necessary now)
    """
    Processes batch of proteins given batch key
    Returns dict mapping protein IDs to processed data
    
    Process
    For each protein in the FASTA file:
      - one-hot-encodes sequences
      - loads the matching NPZ file + processes arrays
      - combines the per-residue features into a sequential tensor
    
    Returns dictionary where key (protein ID) maps to
      - 'input': RNN input tensor (numpy array of shape (L, F))
      - 'target': distance map tensor
      - 'sequence': just in case
      - 'mask1d': for confidence
    """
    
    print("Starting preprocessing")
    
    batch_data = {}
    
    count = 0
    error_log = []
    
    for seq_id in batch_keys:
        sequence = fasta_dict[seq_id]
        npz_path = os.path.join(npz_folder, f"{seq_id}.npz")
        if not os.path.exists(npz_path):
            print(f"WARNING: NPZ file not found for {seq_id}; skipping.")
            continue
        
        # One-hot encode the sequence (shape: (L, d))
        one_hot = one_hot_encode(sequence)
        
        # Process NPZ file (arrays like dssp3, phi, psi, msa, mask, dist_ca)
        features = process_npz(npz_path)
        
        # Create sequential input tensor from per-residue features
        try: # Need try//except here because a single file had an issue??
            input_tensor = create_sequential_features(one_hot,
                                                    features["dssp3"],
                                                    features["phi"],
                                                    features["psi"],
                                                    features["msa"],
                                                    features['mask1d'])
            
            target = features["dist_ca"]
            batch_data[seq_id] = {
                "input": input_tensor,  # Shape: (L, F)
                "target": target,
                "sequence": sequence,
                "mask1d": features['mask1d']
            }
            # may not need sequence or mask1d (for confidence measurement for regions of predicted dist_ca) - kept just in case
            
            count = count + 1
            print(f"{count}. Finished processing protein {seq_id} | Input shape: {input_tensor.shape}, Target shape: {target.shape}")
        except ValueError as e:
            error_message = f"ERROR: Issue processing {seq_id} - {str(e)}"
            print(error_message)
            error_log.append(error_message)
    
    # Log errors to a file for review
    if error_log:
        with open("processing_errors.log", "w") as log_file:
            log_file.write("\n".join(error_log))
        print(f"Logged {len(error_log)} errors to processing_errors.log")
            
        
    print(f"Batch Processed. Total proteins processed: {len(batch_data)}")
    return batch_data    

            


if __name__ == '__main__':
    # Could use argparse here (better programming practice + easier to run script standalone from terminal) - however as this program only needed to be run once I decided not too.
    fasta_file = r'C:\Users\cgwl\Documents\AImino_Training\training_data\final.fasta' 
    npz_folder = r'C:\Users\cgwl\Documents\AImino_Training\training_data\ref_npz' # use ref_npz instead of ref_npz_shortened because no longer need shortened version for CNN
    batch_output_folder = r'C:\Users\cgwl\Documents\AImino_Training\training_data\rnn_data_batches'
    output_file = r'C:\Users\cgwl\Documents\AImino_Training\training_data\rnn_data.pt'
    
    starttime = time.time()
    
    os.makedirs(batch_output_folder, exist_ok=True)
    
    fasta_dict = load_fasta(fasta_file)
    all_seq_ids = list(fasta_dict.keys())
    
    batch_size = 100
    total_proteins = len(all_seq_ids)
    
    number_of_batches = (total_proteins + batch_size - 1) // batch_size # ceiling division
    print(f"Total proteins: {total_proteins} Total batches: {number_of_batches}")
    
    batch_file_paths = []
    
    for batch_index in range(number_of_batches):
        start_index = batch_index * batch_size # calculates starting index in list of protein IDs for the current batch
        end_index = min(start_index + batch_size, total_proteins)
        batch_keys = all_seq_ids[start_index:end_index]
        print(f"\nProcessing batch #{batch_index} (proteins {start_index} to {end_index - 1})")
        
        batch_data = process_batch(fasta_dict, npz_folder, batch_keys)
        
        batch_file = os.path.join(batch_output_folder, f'rnn_data_batch_{batch_index}.pt')
        torch.save(batch_data, batch_file)
        print(f"Saved batch #{batch_index} to {batch_file}")
        batch_file_paths.append(batch_file)
        
        del batch_data
        gc.collect() # garbage collector
        
    endtime = time.time()
    
    print("Preprocessing complete")
    print('time:', endtime-starttime)