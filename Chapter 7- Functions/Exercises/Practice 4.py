#Write a Python program that defines a function to calculate the area of a circle, and then
#calls that function with a given radius.

def calculate_circle_area(radius):
    import math
    return math.pi * radius**2
radius = 9
area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {area:.2f}")
