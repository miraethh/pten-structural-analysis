import requests

uniprot_id = "P60484"

url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"

response = requests.get(url)

if response.status_code == 404:
    print("Old AlphaFold link not found. Trying newer model...")
    
    url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb"
    response = requests.get(url)

response.raise_for_status()

with open("results/PTEN_alphafold.pdb", "wb") as f:
    f.write(response.content)

print("Downloaded AlphaFold structure for PTEN (P60484)")