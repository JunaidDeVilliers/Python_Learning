# collection = single "variable" used to store multiple values
#   Set = {} unordered and immutable, but Add/Remove OK. NO dupllicates
#   Because they are unordered we are not able to index the items in a set

fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)

fruits.add("Pineapple")                             # adds an element to the set
print(fruits)

fruits.pop()                                        # removes whatever element is first from the set
print(fruits)
 
fruits.remove("apple")
print(fruits)

fruits.clear()                                      # clears the set
print(fruits)