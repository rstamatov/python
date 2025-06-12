import numpy as np
import matplotlib.pyplot as plt

f = open("sequences.txt", "r")
sequences = []
for line in f:
    if len(line) > 10:
        sequences.append(line[:-1])



alignment = np.zeros((len(sequences[1]), len(sequences[3])))

for i in range(len(sequences[1])-4):
    for j in range(len(sequences[3])-4):
        if sequences[1][i:i+5] == sequences[3][j:j+5]:
            alignment[i, j] = 1


plt.imshow(alignment)
plt.show()

