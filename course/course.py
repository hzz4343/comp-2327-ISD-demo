"""
Description: Defines the Course class.
Author: Damien Altenburg
"""
from department.department import Department

class Course:
    """Represents a course at an educational institution.
    """

    def __init__(self, name: str, department: Department, credit_hours: int):
        """Initializes a new instance of the Course class.

        Args:
            name (str): The name of the course.
            department (Department): The department the course is delivered.
            credit_hours (int): The number of credit hours.

        Raises:
            ValueError: Raised when the name contains no non-whitespace characters or
                        the credit_credit hours is less than or equal to zero.
            TypeError: Raised when the department or credit_hours is not the expected type.
        """
        if len(name.strip()) == 0:
            raise ValueError("The name cannot be blank.")

        if not isinstance(department, Department):
            raise TypeError(f"The department object must be a Department type.")

        if not isinstance(credit_hours, int):
            raise TypeError(f"The credit_hours object must be an int type.")

        self.__name = name
        self.__department = department
        self.__credit_hours = credit_hours

    @property
    def name(self) -> str:
        """Gets the name of the course.

        Returns:
            The name of the course.
        """
        return self.__name

    @property
    def department(self) -> Department:
        """Gets the department the course is delivered within.

        Returns:
            The faculty department the course is managed from.
        """
        return self.__department

    @property
    def credit_hours(self) -> int:
        """Gets the number of credit hours for this course.

        Returns:
            The number of instructional hours for the course.
        """
        return self.__credit_hours

    def __str__(self) -> str:
        """Returns the "informal" or nicely printable string representation of the object.

        Returns:
            The "informal" or nicely printable string representation of the object."""
        return (
            f"Course: {self.__name}\n"
            f"Department: {self.__department.name.replace('_', ' ').title()}\n"
            f"Credit Hours: {self.__credit_hours}"
        )
        
        