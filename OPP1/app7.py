#Class & instances attributes
class Student:
    college_name = "ABS Collage" 
    # name = "anonymous" #class attr


    #default construct
    def __init__(self):
        print("add new student in Database...")

    #parametrize construct  
    def __init__(self, name, marks):
        print(self)
        self.name = name # obj attr > class attr
        self.marks = marks
        print("adding new student in Database...")
    

s1 = Student("pradip",98)
print(s1.name)
print(s1.marks,s1.college_name)

s2 = Student("Subha",97)
print(s2.name,s2.marks)