import subprocess
import pandas as pd

# Run DSSP and force old DSSP text output format
with open("results/PTEN_dssp.out", "w") as outfile:
    subprocess.run(
        [
            "mkdssp",
            "--output-format=dssp",
            "results/PTEN_alphafold.pdb"
        ],
        stdout=outfile,
        text=True
    )

records = []

with open("results/PTEN_dssp.out") as f:
    started = False

    for line in f:
        if line.startswith("  #  RESIDUE"):
            started = True
            continue

        if started and len(line) > 16:
            residue = line[5:10].strip()
            amino_acid = line[13]
            ss = line[16] if line[16] != " " else "C"

            records.append({
                "residue": residue,
                "amino_acid": amino_acid,
                "ss": ss
            })

df = pd.DataFrame(records)

df.to_csv(
    "results/PTEN_secondary_structure.csv",
    index=False
)

print(df["ss"].value_counts())

rm test_dssp.out