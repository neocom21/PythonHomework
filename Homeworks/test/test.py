class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height  # працює і для квадрата


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Просто передаємо один параметр в обидва


# Перевірка:
square = Square(5)
assert square.calculate_area() == 25