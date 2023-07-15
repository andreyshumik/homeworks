class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, acceleration):
        self.speed += acceleration

    def brake(self, braking):
        self.speed -= braking

    def get_speed(self):
        return self.speed



my_car = Car("BMW", "525", 2000, 110)
print(my_car.get_speed())

my_car.accelerate(50)
print(my_car.get_speed())

my_car.brake(20)
print(my_car.get_speed()) 