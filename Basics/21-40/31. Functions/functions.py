# function = A block of reusable code
#            place () after the function name to invoke it.

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

person = {"Junaid": 26, "Ishaaq":27, "Kyle":25, "Britney": 23}

for name, age in person.items():
    happy_birthday(name, age)