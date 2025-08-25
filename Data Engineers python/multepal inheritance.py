class company():

    def __init__(self,com_name):
        self.com_name =  com_name
        

    def company_info(self):
        print(f"Company Name is {self.com_name}")


class country():

    def __init__(self,country_name):
        self.country_name = country_name

    def country_info(self):
        print(f"Country Name is {self.country_name}")





class employee(company,country):

    def __init__(self,emp_name,com_name,country_name):
        self.emp_name = emp_name

        company.__init__(self,com_name)

        country.__init__(self,country_name)
        # self.com_name = com_name

    def full_info(self):
        print(f"The employee {self.emp_name} lives in {self.country_name} and works for {self.com_name}")

    def all_info_child(self):
        print("This is running from employee")
        company.company_info(self)
        # super().company_info()
        country.country_info(self)
    
    

emp1 = employee("pradip","XYZ","Us")

# emp1.emp_info()
emp1.full_info()
emp1.all_info_child()