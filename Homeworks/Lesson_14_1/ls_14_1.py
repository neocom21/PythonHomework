class GroupLimitError(Exception):
    """Користувацький виняток для перевищення ліміту студентів у групі."""
    pass

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)  # Визиваємо конструктор Human, бо Student
        self.record_book = record_book  # додаємо нове поле специфічне для студента

    def __str__(self):
        return f'{super().__str__()}, Record book: {self.record_book}'

class Group:

    def __init__(self, number, max_value=10):
        self.number = number
        self.group = set()
        self.max_value = max_value

    def add_student(self, student):
        if len(self.group) >= self.max_value:
            raise GroupLimitError("Достигнуто максимальну кількість студентів у групі!")
        self.group.add(student)  # Используем append() вместо add()

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
           self.group.remove(student)


    def find_student(self, last_name):

        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):

        all_students = ''
        i = 1
        for student in self.group:
            line = str(i) + ") " + str(student) + '\n'
            all_students += ' ' + line
            i += 1

        return f'Number Group: {self.number}\n{all_students} '

st1 = Student('Male', 30, 'Steve1', 'Jobs1', 'AN142')
st2 = Student('Female', 25, 'Liza1', 'Taylor1', 'AN145')
st3 = Student('Male', 30, 'Steve2', 'Jobs2', 'AN142')
st4 = Student('Female', 25, 'Liza2', 'Taylor2', 'AN145')
st5 = Student('Male', 30, 'Steve3', 'Jobs3', 'AN142')
st6 = Student('Female', 25, 'Liza3', 'Taylor3', 'AN145')
st7 = Student('Male', 30, 'Steve4', 'Jobs4', 'AN142')
st8 = Student('Female', 25, 'Liza4', 'Taylor4', 'AN145')
st9 = Student('Male', 30, 'Steve5', 'Jobs5', 'AN142')
st10 = Student('Female', 25, 'Liza5', 'Taylor5', 'AN145')
st11 = Student('Male', 30, 'Steve6', 'Jobs6', 'AN142')





gr = Group('PD1')

try:

    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)


    print(gr)

except GroupLimitError as e:
    print(f"Помилка: {e}")



