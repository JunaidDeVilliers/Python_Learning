item = input("What item would you to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"""
      Item: {item}
      Price: {price}
      Quantity: {quantity}
      Total Amount Due: R{total}
""")