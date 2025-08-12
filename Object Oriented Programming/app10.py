#10.Multiple Inheritance
#--Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstring multiple inheritance
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
    

my_tesla = ElectricCar("Tesla","Model S", "85kwh")
# print(my_tesla.fuel_type())

# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))

class  Battery:
    def battery_info(self):
        return"This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
