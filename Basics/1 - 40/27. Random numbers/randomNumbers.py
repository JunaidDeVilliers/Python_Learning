import random

low = 1
high = 100
options = ("rock", "paper", "scissors")

number = random.randint(low, high) #generating a random number between 1 and 6
number2 = random.random() #will return a random floating point number between 0 and 1

option = random.choice(options)

print(option)