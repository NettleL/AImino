import tarfile
import os
import time

archive_path = '/mnt/c/Users/cgwl/Downloads/npz.tar.bz2'
destination_folder = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/npz'
file_list_path = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/fasta_list.txt'


os.makedirs(destination_folder, exist_ok=True)  

file_list = []
with open(file_list_path, 'r') as f:
    for line in f:
        file_list.append(line.strip())
      
print('started')
counter = 0
start_time = time.time()
with tarfile.open(archive_path, 'r:bz2') as tar:
    print('tarfile opened')
    for member in tar.getmembers():
        if os.path.basename(member.name) in file_list:
            tar.extract(member, destination_folder)
            counter += 1
            print(f'extracted {member.name}, count = {counter}')
                
end_time = time.time()
print('complete')
print('time taken =', end_time - start_time)

