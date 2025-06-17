class Vehicle:
    def type(self):
        print("This is a vehicle")


class BMW(Vehicle):
    def car(self):
        print("BMW is a car")


class Honda(Vehicle):
    def bike(self):
        print("Honda is a bike")


c = BMW()
c.type()
c.car()

b = Honda()
b.type()
b.bike()
