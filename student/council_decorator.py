from student.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    @property
    def grade_point_average(self) -> float:
        grade_point_average = super().grade_point_average
        
        increases ={
            4.13: .35,
            3.67: .19,
            2.4: .04
        }
        increases = 0
        for average in increases:
            if grade_point_average > average:
                # grade_point_average += increases[average]
                increases = increases[average]
                break
        
        return grade_point_average