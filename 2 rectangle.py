class Rectangle():
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def get_area(self):        
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)


a = Rectangle(2,5)
print(a.get_area())
print(a.get_perimeter())