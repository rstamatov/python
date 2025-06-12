import numpy as np
import matplotlib.pyplot as plt

sequences = []

f = open(r"C:\Users\stamatov\Desktop\Python seminar\PWMs/sequences.txt")
for line in f:
    tokens = line.split()
    print (tokens)
    sequences.append(tokens[0])

f.close()

N = len(sequences)
L = len(sequences[0])
pwm = np.zeros((4, L))

for i in range(N):
    for j in range(L):
        if sequences[i][j] == "A":
            pwm[0, j] += 1
        elif sequences[i][j] == "C":
            pwm[1, j] += 1
        elif sequences[i][j] == "G":
            pwm[2, j] += 1
        elif sequences[i][j] == "T":
            pwm[3, j] += 1

pwm /= np.sum(pwm, axis = 0)

plt.imshow(pwm)
plt.show()

            

