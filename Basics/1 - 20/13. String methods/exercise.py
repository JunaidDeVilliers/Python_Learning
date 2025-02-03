username = input("Please enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif username.count(" ") > 0:
    print("There can be no spaces in you username")
elif not username.isalpha():
    print("Your username must only contain alphabetic characters")
else:
    print(f"Welcome {username}")