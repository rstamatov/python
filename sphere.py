import numpy as np
import matplotlib.pyplot as plt

##################################################################

def sphere(img, radius, center):
    # Create the sphere
    for i in range(0, 100):
        for j in range(0, 100):

            x = center[0]
            y = center[1]
            
            delta = ((i-x)**2 + (j-y)**2) ** 0.5

            if delta < radius:
                img[i, j] = radius - delta

##################################################################

# create an empty array 100, 100
img = np.zeros((100, 100))

# for цъкъл за локацията

    # вместо [10, 50], напишете текущия център
    sphere(img, 5, [10, 50])

    # Plot
    plt.imshow(img)
    plt.savefig("sphere.png")

###############################################################################


