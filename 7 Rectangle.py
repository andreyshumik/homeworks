# 7. Создайтекласс Rectangle, который будет иметь атрибуты width и height, а также методы get_area() и get_perimeter(), 
# возвращающие площадь и периметр прямоугольника соответственно. Реализуйте также метод is_square(), который будет возвращать True, 
# если прямоугольник является квадратом.

class Rectangle():
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def get_area(self):        
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        if self.width == self.height:
            return True


a = Rectangle(2,5)
print(a.get_area())
print(a.get_perimeter())

b = Rectangle(5,5)
print(b.get_area())
print(b.get_perimeter())
print(b.is_square())