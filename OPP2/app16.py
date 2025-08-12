#Reference Variables
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object

#Object without a reference
class Person:

    def __init__(self):
        self.name = 'nitish'
        self.gender = 'male'

p = Person()
q = p

#Multiple ref
print(id(p))
print(id(q))

print(p.name)
print(q.name)
#Change attribute value with help of 2nd object
q.name = 'ankit'
print(q.name)
print(p.name)