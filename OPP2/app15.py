#How objects access attributes
class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'India':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)


# How to access attributes
p = Person('nitish','india')
print(p.country)
print(p.name)

#How to access methods
print(p.greet())

#Attribute creation from outside of thr class
p.gender = 'male'
print(p.gender)