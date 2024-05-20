import re

def count_pattern_occurrences(sequence, pattern):
    return len(re.findall(pattern, sequence))

def process_fasta(fasta_file, output_file, pattern):
    with open(fasta_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_gene_name = None
        current_sequence = ''
        pattern_count = 0

        for line in infile:
            line = line.rstrip()
            if line.startswith('>'):
                if current_gene_name:
                    # Write the previous gene if it has the pattern
                    if pattern_count > 0:
                        outfile.write(f">>{current_gene_name} count: {pattern_count}\n")
                        outfile.write(f"{current_sequence}\n")
                match = re.match(r">(\S+)", line)
                if match:
                    current_gene_name = match.group(1)
                current_sequence = ''
                pattern_count = 0
            else:
                current_sequence += line
                pattern_count = count_pattern_occurrences(current_sequence, pattern)
        
        # Write the last gene if it has the pattern
        if current_gene_name and pattern_count > 0:
            outfile.write(f">>{current_gene_name} count: {pattern_count}\n")
            outfile.write(f"{current_sequence}\n")

def main():
    pattern = input("Enter the repetitive sequence ('GTGTGT' or 'GTCTGT'): ")
    fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = f"{pattern}_duplicate_genes.fa"
    
    process_fasta(fasta_file, output_file, pattern)
    print(f"The file '{output_file}' has been created with genes containing the repetitive sequence.")

if __name__ == "__main__":
    main()