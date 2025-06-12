# input data
X = [3, 4, 6, 8, 8, 4, -5, -6, -2, -2, 0, 1, 2, 2.5]
Y = [6, 7, 7, 5, 1.5, -3, -3, 3, 5, 8, 6, 4, 3, 2]

# define the empty list
V = []

# Iterate over the input coordinates
for i in range(0, len(X)-1):

    # Take the coordinates of the current point
    x1 = X[i]
    y1 = Y[i]

    # Take the coordinates of the second point
    x2 = X[i+1]
    y2 = Y[i+1]

    # Calculate the distance between the points
    s = ((x2-x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Append to the list
    V.append(s)

# Show the result
print (V)
