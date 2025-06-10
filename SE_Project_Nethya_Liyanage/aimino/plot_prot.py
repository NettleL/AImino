import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import io
import base64
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection



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
 
    # Compute deviations
    diff_x = x - x.mean()
    diff_y = y - y.mean()
    
    # Calculate numerator (covariance)
    covariance = (diff_x * diff_y).sum()
    
    # Calculate denominator (product of standard deviations)
    std_x = np.sqrt((diff_x ** 2).sum())
    std_y = np.sqrt((diff_y ** 2).sum())
    
    return covariance / (std_x * std_y)
    
# ================================
# Main Inference & Visualization
# ================================
def plot(pred_np, target_np, rmse, pearson):
    
    fig = plt.figure(figsize=(14, 10))
    
    # Plot 2D Distance Maps
    ax1 = fig.add_subplot(2, 2, 1)
    im1 = ax1.imshow(pred_np, cmap='viridis', origin='lower')
    ax1.set_title("Predicted Cα Distance Map")
    ax1.set_xlabel("Residue Index")
    ax1.set_ylabel("Residue Index")
    fig.colorbar(im1, ax=ax1)
    
    ax2 = fig.add_subplot(2, 2, 2)
    im2 = ax2.imshow(target_np, cmap='viridis', origin='lower')
    ax2.set_title("Ground Truth Cα Distance Map")
    ax2.set_xlabel("Residue Index")
    ax2.set_ylabel("Residue Index")
    fig.colorbar(im2, ax=ax2)
    
    # Plot 3D Structures
    X_pred = classical_mds(pred_np, ndim=3)
    X_target = classical_mds(target_np, ndim=3)
    
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.scatter(X_pred[:, 0], X_pred[:, 1], X_pred[:, 2], c='teal', label='Predicted')
    ax3.set_title("Predicted 3D Structure (MDS)")
    ax3.set_xlabel("X")
    ax3.set_ylabel("Y")
    ax3.set_zlabel("Z")
    ax3.legend()
    
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.scatter(X_target[:, 0], X_target[:, 1], X_target[:, 2], c='indigo', label='Ground Truth')
    ax4.set_title("Ground Truth 3D Structure (MDS)")
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")
    ax4.set_zlabel("Z")
    ax4.legend()
    
    # Title
    fig.suptitle(f"RMSE: {rmse:.4f} | Pearson's Correlation Coefficient: {pearson:.4f}", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    # Convert the figure to a PNG image + encode it in Base64
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)
    return image_base64