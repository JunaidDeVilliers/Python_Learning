# **kwargs      = allows you to pass multiple keyword-arguments
#                 (when you invoke a function that has *args in its parameters you will pack all of those arguments into a dictionary)
#                 * unpacking operator

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:\t{value}")

print_address(street = "123 Fake St.", 
              apt = "100",
              city = "Detroit", 
              state = "MI", 
              zip = "54321")