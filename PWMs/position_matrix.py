import numpy as np
import matplotlib.pyplot as plt

import logomaker
import pandas as pd
import matplotlib.pyplot as plt

def plot_pwm_logo(pwm):
    """
    Parameters:
    pwm: A position weight matrix, can be a numpy array or a Pandas DataFrame.
         The columns should be nucleotide bases ('A', 'C', 'G', 'T')
         and the rows should correspond to different positions in the sequence.

    Returns:
    None
    """
    # Convert PWM to Pandas DataFrame if it is not already
    if isinstance(pwm, np.ndarray):
        # Assuming the PWM has 4 columns for A, C, G, T
        pwm = pd.DataFrame(pwm, columns=['A', 'C', 'G', 'T'])
    elif not isinstance(pwm, pd.DataFrame):
        raise ValueError("The PWM input must be a numpy array or a pandas DataFrame.")

    # Create a sequence logo.
    logo = logomaker.Logo(pwm)

    # Style the logo
    logo.style_spines(visible=False)
    logo.style_spines(spines=['left', 'bottom'], visible=True)
    logo.ax.set_ylabel("Weight")
    
    # Display the logo plot
    plt.show()


# read the file and extract the sequences
sequences = []

f = open(r"C:\Users\stamatov\Desktop\Python seminar\PWMs/sequences.txt", "r")

for line in f:
    tokens = line.split()
    sequences.append(tokens[0])
f.close()

# Compute the matrix
N = len(sequences)
L = len(sequences[0])
pwm = np.zeros((4, L))

for i in range(N): # traverse every motif
    for j in range(L): # traverse every nucleotide of this motif
        
        if sequences[i][j] == "A":
            pwm[0, j] += 1
        if sequences[i][j] == "C":
            pwm[1, j] += 1
        if sequences[i][j] == "G":
            pwm[2, j] += 1
        if sequences[i][j] == "T":
            pwm[3, j] += 1

pwm = pwm / np.sum(pwm, axis = 0)

print (pwm)
consensus = np.argmax(pwm, axis = 0)
print(consensus)

# Plot the matrix
plt.imshow(pwm)
plt.ylabel("T        G          C         A")
plt.show()

plot_pwm_logo(pwm.T)
