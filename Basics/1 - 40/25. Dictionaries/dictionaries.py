# dictionary = collection of (key:value) pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals.get("USA")) # checking to see if the key is in the dictionary

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany":"Berlin"}) # adding a (key, value) pair
capitals.update({"USA":"Detroit"}) # changing a (key, value) pair

capitals.pop("China") # removing a key value pair

keys = capitals.keys() # gets all the keys in a dictionary
values = capitals.values() # get values
print(keys)

for key in capitals.keys():
    print(key, end=" ")

print()

for value in values:
    print(value, end=" ")

print()

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")
