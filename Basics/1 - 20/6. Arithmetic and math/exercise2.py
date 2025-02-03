import math

a = float(input("Enter the length of side A of the traingle: "))
b = float(input("Enter the length of side B of the traingle: "))

hypotenuse = math.sqrt(a**2 + b**2)
hypotenuse = round(hypotenuse, 2) # Round to 2 decimal places

print(f"The hypotenuse of a traingle with sides {a}cm and {b}cm is {hypotenuse}cm.")