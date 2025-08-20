#2>Class Method and self
#Add a method to the Car class that displays the full name of the car(brand and model)
class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car =Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.full_name())