
class Employee :
    def __init__(self, firstname, lastname, age, cno, email):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.cno = cno
        self.email = email

    def print_details(self):
        print(self.firstname, self.lastname, self.age, self.cno, self.email)
    @property
    def fullname(self):
        return self.firstname+" "+self.lastname
    @fullname.setter
    def fullname(self, fullname): # John Shinde
        self.firstname = fullname.split(" ")[0]
        self.lastname = fullname.split(" ")[1]
        self.email = self.firstname+"."+self.lastname+"@company.com"

    @fullname.deleter
    def fullname(self):
        self.firstname = None
        self.lastname = None
        self.email = None


emp1 = Employee("John", "Wick", 33, 777, 'john.wick@company.com')

emp1.print_details()

emp1.fullname = "Bruce Patil"

emp1.print_details()

del emp1.fullname

emp1.print_details()





