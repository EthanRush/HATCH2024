from Bio import SeqIO
from Bio.pairwise2 import align

# Load the reference genome for MTHFR gene
reference_genome = SeqIO.read("chromosome_1_full_human.fasta", "fasta")

# Load astronaut gene sequences
astronaut_sequences = [SeqIO.read(f"astronaut{i}.fasta", "fasta") for i in range(1, 6)]

# Align each astronaut's gene sequence with the reference genome
alignments = [align.globalxx(reference_genome.seq, astronaut.seq) for astronaut in astronaut_sequences]

# Identify and report variants
for i, astronaut_alignments in enumerate(alignments):
    alignment = astronaut_alignments[0]
    print(f"Astronaut {i+1} alignment to reference:")
    print(alignment)