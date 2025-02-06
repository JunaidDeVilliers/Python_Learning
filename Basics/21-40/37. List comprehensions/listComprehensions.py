# list comprehension = A concise way to create lists in Python
#                      Compact and easier to read then traditional loops
#                      [expression for value in iterable if condition]

doubles = [print(x * 2, end=" ") for x in range(1, 11)]
print()

triples = [print(y * 3, end=" ") for y in range(1, 11)]
print()

squares = [print(z **2, end=" ") for z in range(1, 11)]
print()