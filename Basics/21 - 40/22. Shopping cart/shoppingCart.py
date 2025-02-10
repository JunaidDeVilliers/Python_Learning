foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: R" ))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for x in range(len(foods)):
    print(f"{foods[x]} \t\t:R{prices[x]}")

for price in prices:
    total += price

print("")
print(f"Total\t\t:R{total}")