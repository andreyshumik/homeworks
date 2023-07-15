# 8. Создайте класс Person, который будет иметь атрибуты name и age, а также метод say_hello(), 
# выводящий на экран строку "Привет, меня зовут <name> и мне <age> лет." Реализуйте также метод can_vote(),
# который будет возвращать True, если возраст человека больше или равен 18 лет.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет.')

    def can_vote(self):
        if self.age >= 18:
            return True
        

friend1 = Person('Vasya', 25)
friend1.say_hello()
print(friend1.can_vote())

friend2 = Person('Petya', 17)
friend2.say_hello()
print(friend2.can_vote())