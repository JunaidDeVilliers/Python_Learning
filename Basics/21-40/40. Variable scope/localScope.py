# variable scope = whera a variable is visible and accessible.
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Variables declared in a function are local to that function (have a local scope)
def funct1():
    a = 1
    print(a)

def funct2():
    b = 2
    print(b)

funct1()
funct2()