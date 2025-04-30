'''
RULES
https://github.com/linsalrob/fasta_validator
1. Each header line starts with a >. The header preceedes the sequence.
2. Every other line is considered a sequence line
3. Sequence lines may not contain whitespace, numbers, or non-sequence characters. In other words, they must only contain the characters [A-Z] and [a-z]
4. Sequence lines can end with a new line or return depending on whether you have edited this file on a mac, pc, or linux machine.
5. Sequence lines can be empty.
6. The sequence identifier is the string of characters in the header line following the > and upto the first whitespace. Everything after the first whitespace is descriptive, and can be as long as you like
7. Each sequence identifier must be unique within the fasta file.

RETURN CODES
0 this is a valid fasta file
1 the first line does not start with a > (rule 1 violated).
2 there are duplicate sequence identifiers in the file (rule 7 violated)
3 there are characters in a sequence line other than [A-Za-z]
'''

from Bio import SeqIO

file_path = 'SE Project - Nethya Liyanage/test/ligase0.fasta'
seq_id = [] # list of ids of each sequence in fasta file
seq_count = 0
is_valid = True
dictionary = {}

with open(file_path) as file:
    filelist = file.read().splitlines()

if file_path.endswith(".fasta"):
    if filelist[0][0] == '>': # if the first character of the first line (i.e. the first character) is >
        seq_count = 1 # no. of sequences in fasta file
        line_count = 1 # no. of lines in fasta file
        seq_id.append(filelist[0].split(maxsplit=1)[0]) # add identifier (from > up to first whitespace) to list
        for line in filelist[1:]: # for each line after the first line (seq identifier no. 1)
            line_count = line_count + 1
            if line != '': # if line is not empty
                if line[0] =='>': # if line begins with >, it is a sequence identifier
                    seq_count = seq_count + 1
                    if line.split(maxsplit=1)[0] in seq_id:
                        is_valid = False
                        dictionary[line_count] = 2
                    else:
                        pass
                    seq_id.append(line.split(maxsplit=1)[0])
                elif line.isalpha(): # if line is not sequence identifier, it must pass isalpha
                    dictionary[line_count] = 0
                else:
                    is_valid = False
                    dictionary[line_count] = 3
            else:
                pass # if line is empty, ignore
    else:
        is_valid = False
        dictionary[1] = 1

else:
    is_valid = False
    dictionary['Nil'] = 4
    
# Validity
if is_valid:
    print('VALID')
else:
    print('INVALID')

print('') 
    
# Meta Info
print(f'Sequences: {seq_count}')
for s_id in seq_id:
    print(s_id)

print('') 
    
# Error Messages
for (key, value) in dictionary.items():
    if value == 0:
        pass
    elif value == 1:
        print(f'(Line {key}) Error 1: the first line does not start with a > (rest of file was not read & thus further issues can not be determined)')
    elif value == 2:
        print(f'(Line {key}) Error 2: there are duplicate sequence identifiers in the file')
    elif value == 3:
        print(f'(Line {key}) Error 3: there are characters in a sequence line other than [A-Za-z]')
    elif value == 4:
        print(f'(Line {key}) Error 4: Not a .FASTA file')