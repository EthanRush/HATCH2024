from Bio import SeqIO, pairwise2
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
# Load the reference MTHFR sequence
reference_seq = SeqIO.read("MTHFR_Gene.fasta", "fasta").seq
# List of astronaut FASTA files
astronaut_files = [
    "Astro1_MTHFR.fasta",
    "Astro2_MTHFR.fasta",
    "Astro3_MTHFR.fasta",
    "Astro4_MTHFR.fasta",
    "Astro5_MTHFR.fasta"
]
# Function to align sequences, find nucleotide at position 677, and save as FASTA
def align_and_save_as_fasta(astronaut_file, reference_seq):
    astronaut_seq = SeqIO.read(astronaut_file, "fasta").seq
    astronaut_id = SeqIO.read(astronaut_file, "fasta").id
    # Perform global alignment with a specific scoring scheme
    alignments = pairwise2.align.globalms(astronaut_seq, reference_seq, 2, -1, -0.5, -0.1, one_alignment_only=True)
    # Assuming the first alignment is the best one
    alignment = alignments[0]
    aligned_astronaut_seq, aligned_reference_seq = alignment[0], alignment[1]
    # Create SeqRecord objects for the aligned sequences
    astronaut_record = SeqRecord(Seq(aligned_astronaut_seq), id=astronaut_id, description="Aligned astronaut sequence")
    reference_record = SeqRecord(Seq(aligned_reference_seq), id="Reference_MTHFR", description="Aligned reference sequence")
    # Save the aligned sequences to a FASTA file
    output_file = f"al_{astronaut_file}"
    SeqIO.write([astronaut_record, reference_record], output_file, "fasta")
    print(f"Saved aligned sequences to {output_file}")
# Align each astronaut's sequence, find the nucleotide at position 677, and save as FASTA
for astronaut_file in astronaut_files:
    align_and_save_as_fasta(astronaut_file, reference_seq)







