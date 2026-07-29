import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/PTEN_secondary_structure.csv")

mapping = {
    "H": "Helix",
    "G": "Helix",
    "I": "Helix",
    "E": "Sheet",
    "B": "Sheet",
    "T": "Coil/Turn",
    "S": "Coil/Turn",
    "C": "Coil/Turn"
}

df["category"] = df["ss"].map(mapping).fillna("Other")

counts = df["category"].value_counts()

plt.figure(figsize=(6,4))
counts.plot(kind="bar")

plt.title("PTEN Secondary Structure Composition")
plt.ylabel("Number of residues")
plt.tight_layout()

plt.savefig(
    "results/PTEN_secondary_structure_plot.png",
    dpi=150
)

print("Saved plot!")