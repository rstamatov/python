from tifffile import imread, imsave
import matplotlib.pyplot as plt
import numpy as np
import os

all_files = os.listdir(r"C:\Users\stamatov\Desktop\Lab\RPE1 1770\corrected\for splines length")
volumes = []

for filename in all_files:
    
    # Прочитаме изображение от файл
    img = imread(r"C:\Users\stamatov\Desktop\Lab\RPE1 1770\corrected\for splines length/" + filename)

    # Намираме всички сегментирани обекти 
    all_labels = list(np.unique(img))

    # Махаме фона от списъка
    all_labels.remove(0)

    # Намираме обема на обект с ID 22
    mask = (img == 22)
    volume = np.sum(mask)

    volumes.append(volume)

plt.plot(volumes)
plt.show()



