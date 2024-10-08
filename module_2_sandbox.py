from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id: int):
        self.__employee_id = employee_id
    
    @property
    def employee_id(self):
        return self.__employee_id
    
    @abstractmethod
    def calculate_pay(self):
        pass
    
    def __str__(self):
        return f"Employee: {self.employee_id}"
    
class HourlyEmployee(Employee):
    def __init__(self, employee_id: int, hours: float, rate: float):
        super().__init__(employee_id)
        self.__hours = hours
        self.__rate = rate
        
    def calculate_pay(self):
        return self.__hours * self.__rate
    
    
    def __str__(self):
        return f"HourlyEmployee: {self.__hours} {self.__rate}"      

# Memory
# main: employee = 001
# 001 -> HourlyEmployee (hours, rate)
# 002 -> Employee (employee_id)

class SalaryEmployee(Employee):
    def __init__(self, employe_id: int, annual_salary: float):
        super().__init__(employe_id)
        self.__annual_salary = annual_salary
        
    def calculate_pay(self):
        return self.__annual_salary / 26
    
    def shout(self):
        return 0

def pay_employee(employee: Employee):
    if not isinstance(employee, Employee):
        raise TypeError("Not an employee.")
    
    pay = employee.calculate_pay()
    
    print(f"Employee {employee.employee_id} is paid ${pay:.2f}.")

def main():
    employee = HourlyEmployee(123, 40, 10)
    
    print(employee)
    # 如果employee_id写了accessor,那么就可以用这个去access那个值，但是不能改，如果没写accessor, inheritance也不能查看这个值
    print(type(employee))
    print(isinstance(employee, HourlyEmployee))
    print(isinstance(employee, Employee))
    print(isinstance(employee, str))
    
    salary_employee = SalaryEmployee(345, 26000)
    
    pay_employee(employee)
    pay_employee(salary_employee)
    

if __name__ == "__main__":
    main()