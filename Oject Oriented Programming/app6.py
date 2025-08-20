#6> Class Variables
#Add a cass varible to Car that keeos track if the bumber of ereTED.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        

    def fuel_type(self):
        return "Electric charge"
    

my_tesla = ElectricCar("Tesla","Model S", "85kwh")
print(my_tesla.fuel_type())

safari = Car("TATA", "Safari")
safariThree = Car("Tata", "NEXON")
print(safari.fuel_type())
print(safari.total_car())
print(Car.total_car())