# A 2D list is just a list of lists

groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# print(groceries[0][0]) #row 0, column 0

for collection in groceries:
    for food in collection:
        print(food, end="\t")
    print()