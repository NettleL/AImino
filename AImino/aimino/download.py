import os
import numpy as np
from flask import current_app
from aimino.plot_prot import classical_mds

def create_npz_file(dist_pred, dist_target, xyz_pred, xyz_target, key):
    filename = f'{key}_pred.npz'
    download_folder = current_app.config['DOWNLOAD_FOLDER']
    os.makedirs(download_folder, exist_ok=True)
    file_path = os.path.join(download_folder, filename)
    np.savez(file_path,
             dist_pred=dist_pred,
             dist_target=dist_target,
             xyz_pred=xyz_pred,
             xyz_target=xyz_target)
    return filename