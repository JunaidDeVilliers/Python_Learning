# *args         = allows you to pass multiple non-key arguments
#                 (when you invoke a function that has *args in its parameters you will pack all of those arguments into a tuple)
#                 * unpacking operator
#                 1. positional 2. default 3. keyword 4. ARBITRARY

def add(*args): # name of the parameter isn't as important as the unpacking operator (*)
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5, 6, 7))