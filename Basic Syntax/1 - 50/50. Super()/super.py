# super() = Function used in a child class to call methods from a parent class (superclass).
#           Allows you to extend the functionality of the inherited methods
import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else ' not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {(math.pi * self.radius ** 2):.2f}cm squared")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {(self.width ** 2):.2f}cm squared")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {(0.5 * self.width * self.height):.2f}cm squared")
        super().describe()


circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color="blue", is_filled=False, width=10)
triangle = Triangle(color="green", is_filled=True, width=7, height=10)

print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()
print()

print(square.color)
print(square.is_filled)
print(square.width)
square.describe()
print()

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()