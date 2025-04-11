
# https://www.google.com/search?q=%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%B9+%D0%B4%D1%80%D1%96%D0%B1

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        # a/b * c/d = (a*c) / (b*d)

        chisl = self.a * other.a
        znam = self.b * other.b
        return Fraction(chisl, znam)


    def __add__(self, other):

        # a/b + c/d = (a * d + c * b) / (b * d)

        chisl = self.a * other.b + other.a * self.b
        znam = self.b * other.b
        return Fraction(chisl, znam)


    def __sub__(self, other):

        # a/b - c/d = (a*d - c*b ) / (b*d)

        chisl = self.a * other.b - other.a * self.b
        znam = self.b * other.b
        return Fraction(chisl, znam)


    def __eq__(self, other):
        # a⋅d = c⋅b
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        # a⋅d > c⋅b
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        # a⋅d < c⋅b
        return self.a * other.b < self.b * other.a



    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"





f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'


f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'


f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'


assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True

print('OK')

