import numpy as np
import matplotlib.pyplot as plt

# Load .npz file
data = np.load(r"C:\Users\cgwl\Documents\AImino_Training\training_data_short\ref_npz_s\1a0p_1_A.npz")

distance_matrix = data["dist_ca"]

np.set_printoptions(threshold=np.inf)
print(distance_matrix)


plt.imshow(distance_matrix, cmap="viridis", aspect='auto')
plt.colorbar()
plt.get_current_fig_manager().set_window_title("Distance Map Viewer")
plt.title("Residue-Residue Distance Map")
plt.xlabel("Residue Index")
plt.ylabel("Residue Index")
plt.show()

