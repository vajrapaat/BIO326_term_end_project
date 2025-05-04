import re
import os

filename = input("Enter path to file: ").strip()

def extract_seq_w_spe(fasta_file):
    with open(fasta_file, 'r') as f:
        lines = f.readlines()

    sequences_with_species = []
    sequence = ""
    header = ""

    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            if sequence:
                sequences_with_species.append((header, sequence))
                sequence = ""
            header = line
        else:
            sequence += line

    if sequence:
        sequences_with_species.append((header, sequence))

    return sequences_with_species

seq_w_spe = extract_seq_w_spe(filename)

output_filename = "processed_sequences.fasta"
with open(output_filename, 'w') as f_out:
    for header, seq in seq_w_spe:
        species = re.search(r'OS=([A-Za-z ]+)', header)
        species_name = species.group(1) if species else "Unknown"
        f_out.write(f">{species_name}: {header[1:]}\n{seq}\n")

print(f"Saved as: {output_filename}")
