import math

class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

class Ellipse(Shape):
    def __init__(self, semi_major_axis, semi_minor_axis):
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

    def calculate_area(self):
        return math.pi * self.semi_major_axis * self.semi_minor_axis

# Створення об'єктів
rectangle = Rectangle(4, 5)
circle = Circle(3)
square = Square(4)
ellipse = Ellipse(5, 3)

# Виведення площ
print(f"Area of Rectangle: {rectangle.calculate_area()}")
print(f"Area of Circle: {circle.calculate_area()}")
print(f"Area of Square: {square.calculate_area()}")
print(f"Area of Ellipse: {ellipse.calculate_area()}")
