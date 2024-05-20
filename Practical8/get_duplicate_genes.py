import re
# Regular expression to match the gene name line in the FASTA file (starting with '>')
header_pattern = re.compile(r'^>(.+)')
# Regular expression, used to match and capture gene names
gene_name_pattern = re.compile(r'>(\S+)')
# Initialization variable
current_gene_name = None
gene_sequence = ""
duplication_flag = False
# Open the input FASTA file and the output FASTA file
with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r', encoding='utf-8') as infile, \
     open('duplicate_genes.fa', 'w', encoding='utf-8') as outfile:
    for line in infile:
        line = line.rstrip()
        # Check whether it is the head row of the sequence
        if line.startswith(">"):
            # If the current gene contains 'duplication' and we already have the gene name and sequence, write to the file
            if duplication_flag and current_gene_name:
                outfile.write(f"{current_gene_name}\n{gene_sequence}\n")
                gene_sequence = ""  # Reset sequence string
            # Check if 'duplication' is included, and if so, set the flag
            if "duplication" in line:
                duplication_flag = True
            else:
                duplication_flag = False
            # Match and update the current gene name
            match = gene_name_pattern.match(line)
            if match:
                current_gene_name = match.group(1)
        else:
            # Collect Sequence Data
            if duplication_flag:
                gene_sequence += line
# Ensure that the sequence of the last gene is written (if it exists)
if duplication_flag and current_gene_name:
    with open('duplicate_genes.fa', 'a', encoding='utf-8') as outfile:
        outfile.write(f"{current_gene_name}\n{gene_sequence}\n")