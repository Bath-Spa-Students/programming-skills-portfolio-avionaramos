## Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
Radius = float(input("Radius of a circle: "))
print ("The area of the circle with radius " + str(Radius) + " is: " + str(pi * Radius ** 2))
