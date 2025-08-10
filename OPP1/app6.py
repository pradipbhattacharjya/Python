#Constructor
class Student:

    #default construct
    def __init__(self):
        print("add new student in Database...")

    #parametrize construct  
    def __init__(self, name, marks):
        print(self)
        self.name = name
        self.marks = marks
        print("adding new student in Database...")
    

s1 = Student("pradip",98)
print(s1.name)
print(s1.marks)

s2 = Student("Subha",97)
print(s2.name,s2.marks)