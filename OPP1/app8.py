# Methods
class Student:
    college_name = "ABS Collage"

    #parametrize construct  
    def __init__(self, name, marks):
        print(self)
        self.name = name # obj attr > class attr
        self.marks = marks
        
    def welcome(self):
        print("Welcome student, ", self.name)
    
    def get_marks(self):
        return self.marks
        

s1 = Student("pradip",98)
print(s1.name)
s1.welcome()
print(s1.get_marks())