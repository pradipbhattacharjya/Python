#class method 
class Person:
    name = "anoymous"

    # def changeName(self, name):
    #     self.__class__.name = "Pradip"

    @classmethod
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("pradip bhattacharjya")
print(p1.name)
print(Person.name)