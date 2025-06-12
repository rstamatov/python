import numpy as np
import matplotlib.pyplot as plt
import os



def create_sphere(img, center, radius):

    # Create the sphere
    for i in range(100):
        for j in range(100):

            # Calculate the distance to the center
            center_x = center[0]
            center_y = center[1]

            delta = ((i - center_x) ** 2 + (j - center_y) ** 2) ** 0.5

            if delta < radius:
                img[i, j] = radius-delta


def move_sphere(center, radius):

    x = center[0]
    y = center[1]

    if not os.path.exists("spheres"):
        os.mkdir("spheres")
    
    for t in range(30):
        img = np.zeros((100, 100))
        new_center = [x, y + t]
        create_sphere(img, new_center, 5)

        plt.imshow(img)
        plt.savefig("spheres/t" + str(1000 + t) + ".png")
        plt.cla()

"""
# create an empty array 100, 100
img = np.zeros((100, 100))
create_sphere(img, [20, 20], 5)
create_sphere(img, [20, 30], 5)
create_sphere(img, [30, 50], 5)
"""
img = np.zeros((100, 100))
move_sphere([10, 10], 5)

plt.imshow(img)
plt.show()


###############################################################################


