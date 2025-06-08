import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn.functional as F
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection
from aimino import ProteinStructureModel


# ==========================
# Classical MDS Function
# ==========================
def classical_mds(D, ndim=3):
    # Square the distances
    D_sq = D ** 2
    n = D.shape[0]
    
    # Create centering matrix J
    J = np.eye(n) - np.ones((n, n)) / n
    
    # Compute the double centered matrix
    B = -0.5 * (J @ D_sq @ J)
    
    # Eigen-decomposition of B
    eigenvalues, eigenvectors = np.linalg.eigh(B)
    
    # Sort eigenvalues and eigenvectors in descending order
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # Compute the coordinates using the top 'ndim' eigenvalues/vectors
    L = np.diag(np.sqrt(np.maximum(eigenvalues[:ndim], 0)))
    X = eigenvectors[:, :ndim] @ L
    return X

# ============================================
# Pearson's Correlation Coefficient Function
# ============================================
def pearsons_corr_coef(pred, target):
    # Flatten both tensors to 1D arrays
    x = pred.flatten()
    y = target.flatten()
    
    # Compute means
    x_mean = torch.mean(x)
    y_mean = torch.mean(y)
    
    # Compute deviations
    diff_x = x - x_mean
    diff_y = y - y_mean
    
    # Calculate numerator (covariance)
    covariance = torch.sum(diff_x * diff_y)
    
    # Calculate denominator (product of standard deviations)
    std_x = torch.sqrt(torch.sum(diff_x ** 2))
    std_y = torch.sqrt(torch.sum(diff_y ** 2))
    
    return covariance / (std_x * std_y)
    
# ================================
# Main Inference & Visualization
# ================================
def main():
    model = ProteinStructureModel(
        input_dim=427,
        gru_hidden_dim=16,
        low_rank_dim=16, 
        pairwise_channels=32, 
        dropout_rate=0.05929059580679108
     )
    # If long list of error occurs, adjust the dim numbers to fix
    device = torch.device("cpu")

    state_dict = torch.load(r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\aimino\final_trained_model_cpu.pt', map_location=device)
    model.load_state_dict(state_dict)

    
    model.eval()
    
    test_ds = torch.load(r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\training_data\final_test_dataset.pt', weights_only=False)
    for i in range(5):    
        sample = test_ds[i] # CHANGE PROTEIN HERE
        protein_seq, test_input, test_mask, test_target = sample
        
        # Add a batch dimension and send tensors to the proper device
        test_input = test_input.unsqueeze(0).to(device).float()    # shape: (1, L, features)
        test_mask  = test_mask.unsqueeze(0).to(device)               # shape: (1, L, ...) if needed
        test_target = test_target.unsqueeze(0).to(device).float()    # shape: (1, L, L), a pairwise distance map
                
        with torch.no_grad():
            output = model(test_input, test_mask)
            
        if isinstance(output, tuple):
            dist_ca_map_pred = output[0]
        else:
            dist_ca_map_pred = output
            
        # print("Predicted map statistics:",
        #  "min =", dist_ca_map_pred.min().item(),
        #  "max =", dist_ca_map_pred.max().item(),
        #  "mean =", dist_ca_map_pred.mean().item()) # FOR VALIDATION/TESTING - DELETE
            
        mse_loss = F.mse_loss(dist_ca_map_pred, test_target)
        rmse_loss = torch.sqrt(mse_loss)
        pearsons_corr = pearsons_corr_coef(dist_ca_map_pred, test_target)
                
        print('RMSE:', rmse_loss.item())
        print('Pearsons Coefficient:', pearsons_corr.item())

        
        # Convert outputs to np + remove batch dimension (for visualization)
        dist_ca_map_pred_np = dist_ca_map_pred.squeeze(0).cpu().numpy()
        test_target_np      = test_target.squeeze(0).cpu().numpy()

        # PLOTTING 2D MAPS
            
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
                
        im0 = axes[0].imshow(dist_ca_map_pred_np, cmap='viridis', origin='lower')
        axes[0].set_title("Predicted Cα Distance Map")
        axes[0].set_xlabel("Residue Index")
        axes[0].set_ylabel("Residue Index")
        plt.colorbar(im0, ax=axes[0])
                
        im1 = axes[1].imshow(test_target_np, cmap='viridis', origin='lower')
        axes[1].set_title("Ground Truth Cα Distance Map")
        axes[1].set_xlabel("Residue Index")
        axes[1].set_ylabel("Residue Index")
        plt.colorbar(im1, ax=axes[1])
                
        plt.show()
            
        # PLOTTING 3D COORDINATES
        X_pred = classical_mds(dist_ca_map_pred_np, ndim=3)
        X_gt   = classical_mds(test_target_np, ndim=3)
        
        fig_3d = plt.figure(figsize=(14, 6))

        # Predicted
        ax1 = fig_3d.add_subplot(121, projection='3d')
        #ax1.scatter(X_pred[:, 0], X_pred[:, 1], X_pred[:, 2], c=X_gt[:, 2], cmap='viridis', label='Predicted') # colorful
        ax1.scatter(X_pred[:, 0], X_pred[:, 1], X_pred[:, 2], c='red', label='Predicted')
        ax1.set_title("Predicted 3D Structure (MDS)")
        ax1.set_xlabel("X")
        ax1.set_ylabel("Y")
        ax1.set_zlabel("Z")
        ax1.legend()
                
        # Ground Truth
        ax2 = fig_3d.add_subplot(122, projection='3d')
        #ax2.scatter(X_gt[:, 0], X_gt[:, 1], X_gt[:, 2], c=X_gt[:, 2], cmap='viridis', label='Ground Truth') # colorful
        ax2.scatter(X_gt[:, 0], X_gt[:, 1], X_gt[:, 2], c='blue', label='Ground Truth')
        ax2.set_title("Ground Truth 3D Structure (MDS)")
        ax2.set_xlabel("X")
        ax2.set_ylabel("Y")
        ax2.set_zlabel("Z")
        ax2.legend()
                
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    main()
