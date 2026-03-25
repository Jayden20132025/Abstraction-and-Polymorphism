# Parent class (optional but helps show polymorphism)
class Car:
    def fuel_type(self):
        pass

    def max_speed(self):
        pass


# BMW class
class BMW(Car):
    def fuel_type(self):
        print("BMW fuel type: Petrol / Diesel")

    def max_speed(self):
        print("BMW max speed: 250 km/h")


# Ferrari class
class Ferrari(Car):
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")


# Polymorphism
cars = [BMW(), Ferrari()]

for car in cars:
    car.fuel_type()
    car.max_speed()
    print()