import tarfile

# tar_path = r'c:\Users\cgwl\Downloads\pdb.tar.bz2' # for PDB
tar_path = r'c:\Users\cgwl\Downloads\15051.tar.bz2' # for fasta

destination_folder = r'C:\Users\cgwl\Documents\AImino_Training\training_data'

tar = tarfile.open(tar_path, 'r:bz2')
tar.extractall(destination_folder, filter="data")
tar.close()
