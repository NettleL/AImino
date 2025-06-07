import os
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, random_split
from aimino import ProteinStructureModel

# NOTE
# I used Kaggle Accelerators (GPU T4 x 2) to train my model
# This program only runs a single epoch
# Previously I run multiple epochs at a time
# but it was easier to debug by running a single epoch at a time
# and visualising the output before continuing to train a second epoch

# ============================================================================================
# Weight Initialization
# - Convolutional + Linear layers --> Kaiming initialization (assumes ReLU activations)
# - Recurrent layers --> Xavier (input weights) + orthogonal initialization (hidden weights)
# ============================================================================================
def initialize_weights(model: nn.Module):
    for m in model.modules():
        if isinstance(m, (nn.Conv1d, nn.Conv2d, nn.Conv3d)):
            # For convolutional layers with ReLU activation
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.Linear):
            # For fully connected layers with ReLU activation
            nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            if m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, (nn.LSTM, nn.GRU)):
            for name, param in m.named_parameters():
                if 'weight_ih' in name:
                    # Xavier uniform initialization for input-to-hidden weights
                    nn.init.xavier_uniform_(param.data)
                elif 'weight_hh' in name:
                    # Orthogonal initialization for hidden-to-hidden weights
                    nn.init.orthogonal_(param.data)
                elif 'bias' in name:
                    nn.init.constant_(param.data, 0)
        elif isinstance(m, (nn.BatchNorm1d, nn.BatchNorm2d, nn.LayerNorm)):
            # Set BatchNorm weights to 1 and biases to 0
            nn.init.constant_(m.weight, 1)
            nn.init.constant_(m.bias, 0)

# ===============================================================================
# Geometric‐constraints loss
# - Computes the average squared deviation from `bond_length` between residues   
# ===============================================================================
def geometric_constraints_loss(pred: torch.Tensor,
                               mask: torch.Tensor,
                               bond_length: float = 3.8) -> torch.Tensor:
    mask = mask.bool()
    # Extract distances between residues
    d = torch.diagonal(pred, offset=1, dim1=1, dim2=2)
    # Validity mask
    m = mask[:, :-1] & mask[:, 1:] # selects all valid positions 
    # Squared errors
    err = (d - bond_length) * (d - bond_length) * m.float()
    # Sum and average over positions and batches
    sum_err = err.sum(dim=0)
    count_err = m.float().sum(dim=0).clamp(min=1)
    mean_err_i = sum_err / count_err
    return mean_err_i.mean()

# ========================================================
# Training ( + Validation)
# - with checkpointing (after each epoch or NaN gradient)
# ========================================================
def train_model(model: nn.Module,
                train_loader: DataLoader,
                valid_loader: DataLoader,
                num_epochs: int,
                device: torch.device,
                lambda_geom: float = 0.01, # weight for geometric constraints
                lambda_sym: float = 0.1, # weight for symmetry loss
                lambda_var: float = 0.05, # weight for variance
                alpha_pad:   float = 1e-4, # weight for pad penalty
                lr: float = 1e-3,
                grad_clip_norm: float = 1.0,
                checkpoint_dir: str = "./checkpoints"):
    os.makedirs(checkpoint_dir, exist_ok=True)
    
    print("TRAINING STARTED")
    criterion = nn.MSELoss(reduction='none')
    optimizer = optim.Adam(model.parameters(), lr=lr)
    train_losses, valid_losses = [], []

    for epoch in range(1, num_epochs + 1):
        print(f"Epoch {epoch} has started.")

        # TRAINING
        model.train()
        running_train = 0.0

        for batch_idx, (x, mask, target) in enumerate(train_loader, start=1):
            # list comprehension :) Moves inputs to devies + converts to float tensors
            x = [xi.to(device).float() for xi in x]
            mask = [mi.to(device) for mi in mask]
            target = [ti.to(device).float() for ti in target]

            optimizer.zero_grad()
            loss_all = 0.0

            for xi, mi, ti in zip(x, mask, target):
                out = model(xi.unsqueeze(0), mi.unsqueeze(0))
                if isinstance(out, tuple):
                    dist_map, _ = out
                else:
                    dist_map = out

                # build 2D validity mask - 1 = valid residues & 0 = padding
                m_f = mi.unsqueeze(0).float() # (1, L)
                mask2d = m_f.unsqueeze(1) * m_f.unsqueeze(2) # (1, L, L)


                sq_err   = criterion(dist_map, ti.unsqueeze(0))

                # Create a weight mask - weights residue pairs far apart (represent key structural constraints)
                #   Positions with target > threshold: weight = 2.0 
                #   Otherwise: weight = 1.0
                weight_threshold = 0.1 # Used to assign higher weights (2x) to positions where target distance > 0.1
                weight_mask = ((ti.unsqueeze(0) > weight_threshold).float() * 2 + 
                               (ti.unsqueeze(0) <= weight_threshold).float())

                
                weighted_sq_err = sq_err * weight_mask
                weighted_sq_err_mask = weighted_sq_err * mask2d
        
                
                n_valid = mask2d.sum().clamp(min=1.0) # Normalise to avoid division by zero
                loss_mse = weighted_sq_err_mask.sum() / n_valid
                
                loss_geom = geometric_constraints_loss(dist_map, mi.unsqueeze(0))
                loss_sym = torch.mean(torch.abs(dist_map - dist_map.transpose(1, 2)))
                loss_variance = -torch.var(dist_map)
                
                loss_all += (loss_mse + lambda_geom * loss_geom + lambda_sym * loss_sym + lambda_var * loss_variance)

            loss = loss_all / len(x)
            loss.backward()

            
            total_norm = 0.0
            for p in model.parameters():
                if p.grad is not None:
                    param_norm = p.grad.data.norm(2)
                    total_norm += param_norm.item() ** 2
            total_norm = total_norm ** 0.5
            # print(f"  Batch {batch_idx}: Gradient norm = {total_norm:.4f}")

            # if gradient is Nan, save checkpoint
            if torch.isnan(torch.tensor(total_norm)):
                print("  NaN detected in gradients. Saving checkpoint and stopping training.")
                checkpoint = {
                    'epoch': epoch,
                    'batch': batch_idx,
                    'model_state_dict': model.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'loss': loss.item(),
                }
                checkpoint_path = os.path.join(checkpoint_dir, f'checkpoint_nan_epoch_{epoch}_batch_{batch_idx}.pt')
                torch.save(checkpoint, checkpoint_path)
                print(f"  Checkpoint saved to {checkpoint_path}")
                return train_losses, valid_losses

            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=grad_clip_norm) # performs gradient clipping - prevents Nan
            optimizer.step()

            running_train += loss.item()
            print(f"{loss.item():.4f}") # 4 d.p.

        avg_train = running_train / len(train_loader)
        train_losses.append(avg_train)
        print(f"Epoch {epoch} complete. Average Train Loss: {avg_train:.4f}")

        # VALIDATION
        model.eval()
        running_valid = 0.0
        with torch.no_grad():
            for batch_idx, (x, mask, target) in enumerate(valid_loader, start=1):
                x = [xi.to(device).float() for xi in x]
                mask = [mi.to(device) for mi in mask]
                target = [ti.to(device).float() for ti in target]
                
                loss_all = 0.0
                for xi, mi, ti in zip(x, mask, target):
                    out = model(xi.unsqueeze(0), mi.unsqueeze(0))
                    if isinstance(out, tuple):
                        dist_map, _ = out
                    else:
                        dist_map = out
                    m_f    = mi.unsqueeze(0).float()
                    mask2d = m_f.unsqueeze(1) * m_f.unsqueeze(2)

                    sq_err      = criterion(dist_map, ti.unsqueeze(0))
                    sq_err_mask = sq_err * mask2d
                    
                    n_valid     = mask2d.sum().clamp(min=1.0)
                    loss_mse    = sq_err_mask.sum() / n_valid
                    
                    loss_geom = geometric_constraints_loss(dist_map, mi.unsqueeze(0))
                    loss_sym = torch.mean(torch.abs(dist_map - dist_map.transpose(1, 2)))
                    loss_variance = -torch.var(dist_map)
                    
                    loss_all += (loss_mse + lambda_geom * loss_geom + lambda_sym * loss_sym + lambda_var * loss_variance)
                    
                batch_loss = loss_all / len(x)
                running_valid += batch_loss.item()
                print(f"  Validation Batch {batch_idx} complete.")

        avg_valid = running_valid / len(valid_loader)
        valid_losses.append(avg_valid)
        print(f"Epoch {epoch} Validation complete. Average Valid Loss: {avg_valid:.4f}")

        checkpoint = {
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'train_loss': avg_train,
            'valid_loss': avg_valid,
        }
        checkpoint_path = os.path.join(checkpoint_dir, f'checkpoint_epoch_{epoch}.pt')
        torch.save(checkpoint, checkpoint_path)
        print(f"Checkpoint saved at {checkpoint_path}")

    print("TRAINING COMPLETED")
    return train_losses, valid_losses



if __name__ == "__main__":
    if torch.cude.is_available():
        device = torch.device('cuda') # Used Kaggle GPU
    else:
        device = torch.device('cpu')
    print("Using device:", device) # Kaggle GPU or my CPU

    # Load dataset
    data_file = "/kaggle/input/final-dataset-ii/final_dataset_padded.pt"
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"{data_file} not found.")
    data = torch.load(data_file, weights_only=False)
    print("Dataset loaded.")

    # Convert input and target to FP32
    for p in data:
        data[p]['input'] = data[p]['input'].float()
        data[p]['target'] = data[p]['target'].float()
    
    # Determine the feature dimension from the first protein
    first_protein = next(iter(data))
    feature_dim = data[first_protein]['input'].shape[-1]
    print("Feature dimension determined:", feature_dim)

    # Build full_dataset (tuples) from every protein entry
    full_dataset = []
    for protein_seq, protein_data in data.items():
        input_tensor = protein_data['input']
        mask_tensor = protein_data['mask1d'].clone().detach() # creates copy + removes tracking gradients
        target_tensor = protein_data['target']
        full_dataset.append((protein_seq, input_tensor, mask_tensor, target_tensor))
    print("Built full_dataset with", len(full_dataset), "entries.")

    # Unnecessary (but keep just in case) - handles variable-length data (though data is already padded)
    def collate_fn(batch):
        sequences, inputs, masks, targets = zip(*batch)
        return list(inputs), list(masks), list(targets)

    total = len(full_dataset)
    train_n = int(0.80 * total)
    valid_n = int(0.19 * total)
    test_n = total - train_n - valid_n
    train_ds, valid_ds, test_ds = random_split(full_dataset, [train_n, valid_n, test_n])
    

    refined_test_dataset = [test_ds[i] for i in range(len(test_ds))] # list comprehension :)

    torch.save(refined_test_dataset, '/kaggle/working/test_dataset_yay.pt')
    
    print(f"Dataset split into train: {train_n}, valid: {valid_n}, test: {test_n}")

    train_loader = DataLoader(train_ds, batch_size=2, shuffle=True, collate_fn=collate_fn)
    valid_loader = DataLoader(valid_ds, batch_size=2, shuffle=False, collate_fn=collate_fn)
    test_loader  = DataLoader(test_ds, batch_size=2, shuffle=False, collate_fn=collate_fn)
    print("DataLoaders created.")

    # Epoch Training
    print("\n>>> Initial training (defaults)")
    model = ProteinStructureModel(input_dim=feature_dim).to(device)
    initialize_weights(model)
    num_epochs = 1
    tr_losses, va_losses = train_model(model, train_loader, valid_loader, num_epochs, device,
                                       lambda_geom=0.1, lr=1e-4, grad_clip_norm=0.5)


    torch.save(model.state_dict(), "/kaggle/working/final_trained_model_iv.pt") # Used kaggle to train model
    print("TRAINING ENDED")
