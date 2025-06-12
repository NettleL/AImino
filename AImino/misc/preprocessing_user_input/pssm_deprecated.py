from Bio import AlignIO
from Bio.Align import AlignInfo

file_path = r'C:\Users\nethy\OneDrive\Documents\Nethya\School\Year_12\12SE\6-Nethya-Liyanage\SE_Project_Nethya Liyanage\test\msa.afa'
alignment = AlignIO.read(file_path, 'fasta')
summary_align = AlignInfo.SummaryInfo(alignment)
pssm = summary_align.pos_specific_score_matrix(summary_align.dumb_consensus())
print(pssm)