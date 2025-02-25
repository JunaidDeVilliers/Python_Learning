# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name? ")
age = int(input("How old are you? ")) # typecasting the age variable to int since user input it string

print(f"Hello {name}. You are {age} years old.")
print(f"Next year you will be {age + 1} years old.")
