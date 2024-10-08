class SingletonStudentManager:
        # Static (Class) Variables
    __instance = None
    __next_student_number = 20240000
        
    def __new__(cls):   
        # if not None
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def get_student_number(self) -> int:
        current_student_number = self.__next_student_number
        
        self.__next_student_number += 1
        
        return current_student_number