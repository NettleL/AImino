import re # Import regular expressions module for pattern matching
import numpy as np
import torch

# Note: Residue refers to an amino acid

# Constants: due to fixed HHM file format
emission_val_no = 20 # Expected no. of emission probability tokens per residue
emission_start_index = 2 # Emission tokens start after residue letter & residue index
expected_transition_tokens = 10 # Expected no. of tokens on the transition line (including gap penalties)

def parse_hhm(hhm_file):
    '''
    Parses HHM file (from HH-suite). Extracts
    1. Emission probabilities: Per-residue scores for each of the 20 amino acids
    2. Transition probabilities: Values for state transitions (includes gap penalties)
    
    Note: Assumes that each residue block consists of
    • A line beginning with residue letter & index followed by 20 emission tokens
    • The following non-empty line with 10 transition tokens
    Validation checks ensure that emission & transition token counts meet expected numbers.
    
    Returns:
    • emissions (list of lists): List of emission probability vectors (one per residue)
    • transitions (list of lists): List of transition probability vectors
    '''
    
    emissions = []
    transitions = []
    
    # Regular expression to identify residue lines
    residue_line_pattern = re.compile(r'^[A-Z]\s+\d+')
    
    with open(hhm_file, 'r') as file:
        lines = file.readlines()
        
    index = 0 #initialise index for iterating through file lines
    
    while index < len(lines): # Loops through each line in file
        line = lines[index].strip()
        
        # if line matches residue_line_pattern criteria 
        if residue_line_pattern.match(line):
            tokens = line.split()
            
            if len(tokens) < emission_start_index + emission_val_no:
                print(f'Warning: Emission line at index {index} has insufficient tokens. Skipping')
                index += 1
                continue
            emission_values = []
            for token in tokens[emission_start_index: emission_start_index + emission_val_no]:
                try:
                    e_value = float(token)
                except ValueError:
                    e_value = 1e-6 # Small default value
                
                emission_values.append(e_value)
            emissions.append(emission_values) 
            
            # Move to next line to look for transition probabilities
            index +=1
            while index < len(lines) and not lines[index].strip():
                index += 1 # Skip empty lines
            
            if index < len(lines):
                transition_probability_line = lines[index].strip()
                transition_probability_tokens = transition_probability_line.split()
                
                if len(transition_probability_tokens) != expected_transition_tokens:
                    print(f'Warning: Transition line at index {index} has incorrect number of tokens. Will pad/truncate as necessary')
                
                transition_values = []
                for token in transition_probability_tokens[:expected_transition_tokens]:
                    try:
                        t_value = float(token)
                    except ValueError:
                        t_value = 1e-6 # Small default value
                    
                    transition_values.append(t_value)
                
                while len(transition_values) < expected_transition_tokens:
                    transition_values.append(1e-6)
                
                transitions.append(transition_values)
        index +=1
    return emissions, transitions

def normalise(emission_list, transition_list):
    laplace_smoothing_factor = 1.0
    
    emission_array = np.array(emission_list)
    transition_array = np.array(transition_list)
    
    emission_array += laplace_smoothing_factor
    transition_array += laplace_smoothing_factor
    
    emission_logged = np.log(emission_array + 1e-3)
    
    row_sums_emission = emission_logged.sum(axis=1, keepdims=True)
    row_sums_transition = transition_array.sum(axis=1, keepdims=True)
    
    normalised_emission = emission_logged/row_sums_emission
    normalised_transition = transition_array/row_sums_transition
    
    normalised_emission_tensor = torch.tensor(normalised_emission, dtype=torch.float32)
    normalised_transition_tensor = torch.tensor(normalised_transition, dtype=torch.float32)
    
    return normalised_emission_tensor, normalised_transition_tensor
ef, tf = parse_hhm(r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya_Liyanage\test\hhm.hhm')
nef, ntf = normalise(ef, tf)
print('Emission')
print(nef)
print('Transition')
print(ntf)
            
            
            