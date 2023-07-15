# 10. Создайте класс Employee, который будет иметь атрибуты name, position и salary, а также методы get_salary(), 
# возвращающий зарплату работника, и get_tax(), возвращающий сумму налога на зарплату (20% от зарплаты).


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salart(self):
        return self.salary
    
    def get_tax(self):
        return self.salary * 0.2
    

alex = Employee('Alex', 'teacher', 20000)
print(alex.get_salart())
print(alex.get_tax())