from Bio import SeqIO

max_length = 600

input_file = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/cd_hit_ref/7p.fasta' # fasta file after cd-hit refinement qitt 0.7 (from misc_cmd_prompt)
output_file = '/mnt/c/Users/cgwl/Documents/AImino_Training/training_data/len_ref/7p_s.fasta'

filtered_seq = []

with open(input_file, 'r') as file:
    for record in SeqIO.parse(file, 'fasta'):
        sequence_length = len(record.seq)
        
        if sequence_length <=max_length:
            filtered_seq.append(record)

SeqIO.write(filtered_seq, output_file, 'fasta')

# conda run python len_ref.py