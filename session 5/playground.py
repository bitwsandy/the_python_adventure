class Employee :
    def __init__(self,name, email):
        self.name = name
        self.email = email
    def display_info(self):
        print(f"Name : {self.name}, email : {self.email}")

class Developer(Employee):
    def __init__(self, name, email, programming_language):
        super().__init__(name, email)
        self.programming_language = programming_language
    def display_info(self):
        super(Developer, self).display_info()
        print(f"Programming Language : {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, email, emp_list=None):
        super().__init__(name, email)
        if emp_list == None:
            self.emp_list=[]
        else :
            self.emp_list = emp_list

    def add_emp(self,emp):
        if emp not in self.emp_list :
            self.emp_list.append(emp.name)

    def rem_emp(self, emp):
        if emp in self.emp_list :
            self.emp_list.remove(emp.name)

    def display_info(self):
        super().display_info()
        print(f"Number of employees under {self.name} : {self.emp_list}")

emp_1 = Employee("XYZ", "xyz@abc.com")
# print(type(emp_1))

dev_1 = Developer("John","john@gmail.com","python")
dev_1.display_info()

mgr_1 = Manager("Bob", "bob@gmail.com")
mgr_1.display_info()
mgr_1.add_emp(emp_1)
mgr_1.add_emp(dev_1)
print('\n')
mgr_1.display_info()


# Polymorphism : NAAM EK KAM ANEK

