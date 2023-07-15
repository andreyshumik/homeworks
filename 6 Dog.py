# 6. Создайте класс Dog, который будет иметь атрибуты name, breed и age, а также методы bark(), 
# выводящий на экран строку "Гав-гав!" и метод get_human_age(), 
# возвращающий возраст собаки в "человеческих" годах (приблизительно).

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return 'Gav-gav!'

    def get_human_age(self):
        print(f'Sobaka {self.name} vozrastom {self.age} v pereschete na cheloveka imeet vozrast {self.age*7}')


bobik = Dog('Bobik', 'mops', 5)
print(bobik.bark())

bobik.get_human_age()