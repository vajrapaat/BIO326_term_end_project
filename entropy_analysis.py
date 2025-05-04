import os
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
def shannon_entropy(column):
    freqs = defaultdict(int)
    for residue in column:
        freqs[residue] += 1
    total = len(column)
    entropy = 0
    for freq in freqs.values():
        p = freq / total
        entropy -= p * np.log2(p)
    return entropy

filename = input("Enter path to MSA file: ").strip()

sequences = []
with open(filename) as f:
    lines = f.read().splitlines()
    for i in range(0, len(lines), 2):
        seq = lines[i+1].strip()
        sequences.append(seq)


msa_array = np.array([list(seq) for seq in sequences])

entropies = []
for i in range(msa_array.shape[1]):
    column = msa_array[:, i]
    entropies.append(shannon_entropy(column))

plt.figure(figsize=(16, 4))
plt.plot(entropies, label="Shannon Entropy")
plt.xlabel("Residue Position")
plt.ylabel("Entropy")
plt.title("Conservation Analysis Across MSA")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
