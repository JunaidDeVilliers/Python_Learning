# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with coe reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow! Meow!")

class Mouse(Animal):
    def squeak(self):
        print("Squeak! Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.bark()
print()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.meow()
print()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.squeak()
print()