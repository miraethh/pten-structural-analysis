from Bio import SeqIO

record = SeqIO.read("results/PTEN_mRNA.fasta", "fasta")
seq = record.seq

def find_longest_orf(seq):
    best_orf = ""

    for frame in range(3):
        trans = str(seq[frame:].translate(to_stop=False))
        codons = trans.split("*")

        for chunk in codons:
            start = chunk.find("M")

            if start != -1:
                candidate = chunk[start:]

                if len(candidate) > len(best_orf):
                    best_orf = candidate

    return best_orf


protein = find_longest_orf(seq)

print(f"Longest ORF protein length: {len(protein)} aa")

with open("results/PTEN_protein.fasta", "w") as f:
    f.write(">PTEN_predicted_protein\n")
    f.write(protein + "\n")