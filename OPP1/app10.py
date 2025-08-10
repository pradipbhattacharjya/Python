#Static Methods
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
#Static Methods
    @staticmethod#decorator
    def hello():
        print("hello")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"Your avg score is:",sum/3)



s1 = Student("Pradip",[98,79,80])
print(s1.name,s1.marks)
s1.get_avg()
s1.hello()
s1.name = "Subha"
s1.get_avg()