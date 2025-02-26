import math

radius = float(input("Enter the radius of the circle: "))

circumference = round(2 * math.pi * radius, 2) # Also rounding to 2 digits
area = round(math.pi * radius**2, 2) # Also rounding to 2 digits

print(f"The circumference of a circle with radius {radius} is {circumference}cm, and the area is {area}cm\u00B2.")