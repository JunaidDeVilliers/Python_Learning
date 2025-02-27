name = input("Enter your full name: ")

result = len(name) # shows you the length of the string (includes spaces)
result2 = name.find("i") # will return the first occurence of a given character (starts counting at 0)
result3 = name.rfind("i") # will return the last occurence of a given character (starts counting at 0)
# if find() fails to locate a given character it will return -1

print(result)
print(result2)
print(result3)