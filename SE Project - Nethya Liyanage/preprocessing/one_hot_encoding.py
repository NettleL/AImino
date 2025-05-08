import numpy as np
import torch

def one_hot_encoding(fasta_file_path):
    sequence = ''
    
    with open(fasta_file_path, 'r') as file:
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    
    amino_acids = 'ABCDEFGHIKLMNPQRSTVWYZ' # Added B & Z (special cases)
    identity_matrix = np.eye(len(amino_acids))
    encoding_dict ={}
    
    for index in range(len(amino_acids)):
        aa = amino_acids[index]
        encoding_dict[aa] = identity_matrix[index]
    
    encoded_sequence = []
    
    for aa in sequence:
        if aa in encoding_dict:
            encoded_sequence.append(encoding_dict[aa])
        else:
            encoded_sequence.append(np.zeros(len(amino_acids)))
    
    # Converting array to tensor
    # converting array -> np array -> tensor faster than turning sequence directly into tensor
    encoded_sequence_array = np.array(encoded_sequence) 
    encoded_sequence_tensor = torch.tensor(encoded_sequence_array, dtype=torch.float32)
    
    return encoded_sequence_tensor

print(one_hot_encoding(r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year 12\12SE\6-Nethya-Liyanage\SE Project - Nethya Liyanage\test\ligase0.fasta'))
    