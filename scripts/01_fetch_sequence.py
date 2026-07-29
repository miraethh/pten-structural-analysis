from Bio import Entrez, SeqIO
import os

Entrez.email = "nikainamarsya@gmail.com"

handle = Entrez.esearch(
    db="nucleotide",
    term="PTEN[Gene] AND Homo sapiens[Organism] AND RefSeq[Filter] AND mRNA[Filter]",
    retmax=1,
    sort="relevance"
)

record = Entrez.read(handle)
seq_id = record["IdList"][0]

handle = Entrez.efetch(
    db="nucleotide",
    id=seq_id,
    rettype="fasta",
    retmode="text"
)

seq_record = SeqIO.read(handle, "fasta")

os.makedirs("results", exist_ok=True)

with open("results/PTEN_mRNA.fasta", "w") as f:
    SeqIO.write(seq_record, f, "fasta")

print(f"Fetched: {seq_record.id}, length {len(seq_record.seq)} bp")