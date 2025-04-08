from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # Визиваємо конструктор Human, бо Student
        self.record_book = record_book  # додаємо нове поле специфічне для студента

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'

    def __eq__(self, other):
        return isinstance(other, Student) and str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

