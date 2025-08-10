#Abstraction & encapsulation

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    #Abstraction
    def start(self):
        self.acc = True
        self.brk = True
        print("car started...")


car1 = Car()

car1.start()