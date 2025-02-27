# Typecasting is the process of converting a variable from one data type to another

name = "Junaid De Villiers"
age = 26
gpa = 3.2
is_student = True

print(f"Name: {name}")
print(type(name))
name = bool(name)
print(f"After typecasting: {name}")
print(type(name), "\n")
# If you typecasting a nonempty string as a boolean it will return true, and empty string will return false

print(f"Age: {age}")
print(type(age))
age = float(age)
print(f"After typecasting: {age}")
print(type(age), "\n")

print(f"GPA: {gpa}")
print(type(gpa))
gpa = int(gpa) # typecasting gpa to int
print(f"After typecasting: {gpa}")
print(type(gpa), "\n")

print(f"Is student: {is_student}")
print(type(is_student))