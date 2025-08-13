#Inheritance
# parent
class User:

    def __init__(self):
        self.name = 'nitish'

    def login(self):
        print('login')
# child 
class Student(User):

    def __init__(self):
        self.rollno = 100

    def enroll(self):
        print('enroll into the coure')

u = User()
s = Student()

print(u.name)
print(s.login())
print(s.enroll())