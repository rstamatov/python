import matplotlib.pyplot as plt


f = open(r"C:\Users\stamatov\Desktop/" + "focus_track.mdf", "r")

x_coordinates = []
y_coordinates = []



for line in f:
    tokens = line.split(" ")

    if tokens[0] == "Point":
        x_coordinates.append(float(tokens[2]))
        y_coordinates.append(float(tokens[3]))


f.close()

plt.plot(x_coordinates, y_coordinates)
plt.show()





