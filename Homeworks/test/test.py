def capture_stdout(func):
    return func()  # Просто викликаємо функцію та повертаємо її результат


class A:
    def show(self):
        return "A"


class B(A):
    def show(self):
        return "B"


class C(A):
    def show(self):
        return "C"


class D(B, C):
    def show(self):
        return "D"


# Перевірка
obj_D = D()
output_D = capture_stdout(obj_D.show)
assert output_D == 'D'