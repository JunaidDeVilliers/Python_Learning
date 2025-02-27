# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book

# class =  (blueprint) used to design the structure and layout of an object

# methods are actions that an object can perform

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} is moving")

    def stop(self):
        print(f"The {self.color} {self.model} stopped")

    def describe(self):
        print(f"{self.model} is a {self.year} {self.color} car")

