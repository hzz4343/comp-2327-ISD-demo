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
    
# 这里的思路是，我新建一个用来编号的class,这个编号的class只能被创建出一个instance。
# 这个class只有一个功能，就是创建编号，单独拎出来的原因是我只希望创造有且只有一个这个class的object（编号系统）。