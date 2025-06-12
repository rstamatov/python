def cyllinder (R, h, pi = 3.14):
    V = pi * (R**2) * h
    S = 2 * pi * (R**2) + 2 * pi * R * h

    print (V)
    print (S)

    return V, S


radius = input("въведете радиус:")
height = input("въведете височина:")

radius = float(radius)
height = float(height)

V1, S1 = cyllinder(R = radius, h = height, pi = 3.1419)





    
