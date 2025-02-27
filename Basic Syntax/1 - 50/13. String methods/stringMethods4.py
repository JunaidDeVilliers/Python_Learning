phone_number = input("Enter your phone number: ")

result = phone_number.count(" ") # counting the amount of spaces in a phone number
result2 = phone_number.replace(" ", "-") # replacing spaces with dashes
# you can remove a character completely by replacing it with an empty string

print(result)
print(result2)