# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK

fruits = ["apple", "orange", "banana", "coconut"]


for fruit in fruits:
    print(fruit, end=" ")

print(len(fruits))                                  # prints the amount of items in the list
print("apple" in fruits)                            # returns true if apple is in fruits


def print_fruits(fruits):
    for x in range(len(fruits)):
        if x == len(fruits)-1:
            print(f"{fruits[x]}.")
        else:
            print(f"{fruits[x]}, ", end="")


fruits[0] = "pineapple"                             # changes the element at [0]
print_fruits(fruits)

fruits.append("apple")                              # adds an element to the end of the list
print_fruits(fruits)

fruits.remove("pineapple")                          # removes an element
print_fruits(fruits)

fruits.insert(2, "pear")                            # inserting a value at index 2
print_fruits(fruits)

fruits.sort()                                       # sorts the list
print_fruits(fruits)

fruits.reverse()                                    # reverses the elements in the list
print_fruits(fruits)

print(fruits.index("apple"))                        # checking the index of the element apple (where it is on the list)
print(fruits.count("apple"))                        # counting the amount of the specified element in the list

fruits.clear()                                      # clears the list of fruits
print(fruits)