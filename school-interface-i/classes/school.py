from classes.staff import Staff
from classes.student import Student

class School:

    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def __str__(self):
        return f"""{self.name}
---------------
age: {self.age}
id: {self.student_id}"""

    def list_students(self):
        for idx, stud in self.students:
            print(f'{idx + 1}. {stud.name} {stud.school_id}')