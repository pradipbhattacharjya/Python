#Property Decorators
#--Use a property decorator in the Car class to make the model attribute read _only

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    def model(self):
        return self.__model
    



class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
        
    @property
    def fuel_type(self):
        return "Electric charge"
    

# my_tesla = ElectricCar("Tesla","Model S", "85kwh")
# print(my_tesla.fuel_type())

my_car = Car("tata", "Safari")
# my_car.model = "City"
Car("Tata","Nexon")

print(my_car.model)

# print(my_car.general_description())
# print(Car.general_description())