class employee():
    company_name = "xyz"

    def __init__(self,emp_name,emp_dept):
        self.emp_name = emp_name
        self.emp_dept = emp_dept
    
    @property#getter
    def info(self):
        print(f"Employee {self.emp_name} works for {self.emp_dept} in {self.company_name}")


    @info.setter
    def info(self,new_empdetails):
        new_empname = new_empdetails[0]
        new_empdept = new_empdetails[1]


        self.emp_name = new_empname
        self.emp_dept = new_empdept




    # def changeinfo(self,new_empname, new_empdept):
    #     self.emp_name = new_empname
    #     self.emp_dept = new_empdept

    @classmethod
    def changesInClass(self,new_company):
        self.company_name = new_company

    #static Method
    @staticmethod
    def addition(x,y):
        print(x+y)


emp1 = employee("subha","IT")
emp2 =employee("Pradip","HR")

emp1.changesInClass("NewNewCompany")

# print(emp1.company_name)
# emp1.addition(1,2)
# emp1.changes('New company')

# emp2.info()

# emp1.info()
# emp1.changeinfo("subha","HR")
# emp1.info()

emp1.info()

emp1.info["sudip","HR"]

print(emp1.info)