#1.Basic Class and Object
#--Create a Car class with attributes like brand and model.Then create an instance of this classs.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    

my_car = Car("Toyota", "Corolla")
print(my_car.brand)

my_car =Car("TATA", "Safari")
print(my_car.brand)