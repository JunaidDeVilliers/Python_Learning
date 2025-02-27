# Enclosed is when a function is defined inside another function. The inner function has access to the outer function's variables.
# Global scope is when a variable is declared outside a function. It is accessible to all functions.
# If there is a variable with the same name in both the global and local scope, the local variable takes precedence.
def funct1():
    print(x)

def funct2():
    print(x)

x = 3

funct1()
funct2()