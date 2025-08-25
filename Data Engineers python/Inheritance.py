class company():

    def __init__(self,com_name,country):
        self.com_name =  com_name
        self.country = country

    def company_info(self):
        print(f"Company Name is {self.com_name} in {self.country}")


class employee(company):

    def __init__(self,emp_name,com_name,country):
        self.emp_name = emp_name

        company.__init__(self,com_name,country)
        # self.com_name = com_name

    def emp_info(self):
        print(f"Employee Name is {self.emp_name}")

    def company_info_child(self):
        print("This is running from employee")
        company.company_info(self)
        # super().company_info()
    
    

emp1 = employee("pradip","XYZ","USA")

# emp1.emp_info()
emp1.company_info_child()
