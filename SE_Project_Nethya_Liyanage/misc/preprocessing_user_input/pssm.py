from Bio import Align
from Bio.motifs import Motif

file_path = r"C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya Liyanage\test\msa.afa"
alignment = Align.read(file_path, 'fasta')

motif = Motif("ACDEFGHIKLMNPQRSTVWY", alignment)

pssm_counts = motif.counts

probabilities = pssm_counts.normalize(pseudocounts=1e-6)

# CHANGE BASED ON TYPICAL FREQ --> SEE ACADEMIC TEXTS
background_freq = {
    "A": 0.08, "C": 0.02, "D": 0.05, "E": 0.06, "F": 0.04,
    "G": 0.07, "H": 0.02, "I": 0.06, "K": 0.06, "L": 0.09,
    "M": 0.02, "N": 0.04, "P": 0.05, "Q": 0.04, "R": 0.05,
    "S": 0.07, "T": 0.06, "V": 0.07, "W": 0.01, "Y": 0.03
}

pssm = probabilities.log_odds(background=background_freq)

print(pssm)