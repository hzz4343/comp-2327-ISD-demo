from student.student_decorator import StudentDecorator

class CouncilDecorator(StudentDecorator):
    @property
    def grade_point_average(self) -> float:
        grade_point_average = super().grade_point_average
        
        # Dictionary of GPA thresholds and their corresponding increases
        increases = {
            4.13: 0.35,
            3.67: 0.19,
            2.4: 0.04
        }
        
        # Iterate over the thresholds to apply the correct increase
        for average, increase in increases.items():
            if grade_point_average > average:
                grade_point_average += increase
                break  # Exit loop once the first match is found
        
        return grade_point_average
