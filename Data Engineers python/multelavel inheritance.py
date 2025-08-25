class company():

    def __init__(self,com_name):
        self.com_name =  com_name
        

    def company_info(self):
        print(f"Company Name is {self.com_name}")



class  departmant(company):

    def __init__(self,dept_name,com_name):
        self.dept_name = dept_name
        company.__init__(self,com_name)

    def department_info(self):
        print(f"The departmet  is {self.dept_name} of {self.com_name}")

class employee(departmant):

    def __init__(self,emp_name,dept_name,com_name):
        self.emp_name = emp_name

        departmant.__init__(self,dept_name,com_name) 

    def all_info(self):
        print(f"The department is {self.dept_name} of {self.com_name}.Employee name is {self.emp_name}")
    

emp1 = employee("pradip","HR","ABC")

emp1.all_info()
emp1.department_info()
emp1.company_info()