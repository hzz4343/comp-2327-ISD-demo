from student.student_decoratbale import StudentDecoratable

class StudentDecorator(StudentDecoratable):
    def __init__(self, student):
        self.__student = student
    
    def grade_point_average(self) -> float:
        return self.__student.grade_point_average