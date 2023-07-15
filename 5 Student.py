# 5. Создайте класс Student, который будет иметь атрибуты name, age и grades, а также метод add_grade(), 
# добавляющий оценку в список, метод get_average_grade(), возвращающий среднюю оценку, и метод is_honors_student(), 
# возвращающий True, если средний балл выше 4.5.b


class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def is_honors_student(self):
        if self.get_average_grade() > 4.5:
            return True
        else:
            return False
        

bob = Student('Bob', 20, [5.5,4,2,6,5])
bob.add_grade(5)
print(bob.get_average_grade())
print(bob.is_honors_student())