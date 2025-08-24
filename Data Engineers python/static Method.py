class employee():
    company_name = "xyz"

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept
    
    def changes(self,new_company):
        employee.company_name = new_company

    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} in {self.company_name}")

    #static Method
    @staticmethod
    def addition(x,y):
        print(x+y)


emp1 = employee("subha","IT")
emp2 =employee("Pradip","HR")

emp1.addition(1,2)
# emp1.changes('New company')

# emp2.info()
