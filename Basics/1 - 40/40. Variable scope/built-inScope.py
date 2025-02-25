from math import e

# Variables can have the same name as long as they are in different scopes.
# Using (LEGB) the prgram will look for the variable in the local scope first, then the enclosed scope, then the global scope, and finally the built-in scope.
def func1():
    print(e)

e = 3

print(e)
func1()