
from exceptions import GroupLimitError


class Group:
    max_value = 10  # атрибут класу

    def __init__(self, number):
        self.number = number
        self.group = set()


    def add_student(self, student):
        if len(self.group) >= Group.max_value:
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
