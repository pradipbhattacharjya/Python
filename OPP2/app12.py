class Emplpyee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("selary =", self.salary)

class Engineer(Emplpyee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT", "75,000")

engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()