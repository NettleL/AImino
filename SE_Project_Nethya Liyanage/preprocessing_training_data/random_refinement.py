import random
from Bio import SeqIO

input_file = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/len_ref/7p_s.fasta'
output_file = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/final.fasta'
target_count = 6000

sequences = list(SeqIO.parse(input_file, 'fasta'))
current_count = len(sequences)

if current_count <= target_count:
    selected_sequences = sequences
else:
    selected_sequences = random.sample(sequences, target_count)
    
SeqIO.write(selected_sequences, output_file, 'fasta')

# conda run python random_ref.py