fastas = r'C:\Users\cgwl\Documents\AImino_Training\training_data\final.fasta'
file_list_path = r'C:\Users\cgwl\Documents\AImino_Training\training_data\fasta_list.txt'

file_list = []
with open(fastas, 'r') as file:
    for line in file:
        if '>' in line:
            header = line.strip()[1:] + '.npz'
            file_list.append(header)

with open(file_list_path, 'w') as f:
    for filename in file_list:
        f.write(filename + '\n')




