import numpy as np
import os

input_folder = r'C:\Users\cgwl\Documents\AImino_Training\training_data\npz\npz'
output_folder = r'C:\Users\cgwl\Documents\AImino_Training\training_data\ref_npz'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)
    data = np.load(filepath)
    
    new_filepath = os.path.join(output_folder, filename)
    np.savez(new_filepath, dssp3=data['dssp3'], phi=data['phi'], psi=data['psi'], mask1d=data['mask1d'], dist_ca=data['dist_ca'], msa=data['msa'])
    # data.close() # necessary??
    print('extracted', filename)
    
print('extraction complete')