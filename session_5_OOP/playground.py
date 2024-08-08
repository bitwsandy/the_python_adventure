class Employee:
    def __init__(self, first, last, age=25):
        self.first = first
        self.last = last
        self.age = age


    # Property for the email
    @property
    def email(self):
        """Generate email dynamically from first and last name."""
        return f"{self.first.lower()}.{self.last.lower()}@company.com"

    # Property for the full name
    @property
    def fullname(self):
        """Return the full name."""
        return f"{self.first} {self.last} age is {self.age}"

    # Setter for the full name
    @fullname.setter
    def fullname(self, name):
        """Allow setting full name, which updates first and last names."""
        first, last = name[0].split()
        self.first = first
        self.last = last
        self.age = name[1]
    #
    # Deleter for the full name
    @fullname.deleter
    def fullname(self):
        """Delete the full name and reset first and last names to None."""
        print("Deleting Name!")
        self.first = None
        self.last = None

# Example usage
emp_1 = Employee('John', 'Doe', 25)

print(emp_1.email, '||',  emp_1.fullname)

emp_1.fullname = ["Peter Parker",27]

print(emp_1.email, '||',  emp_1.fullname)

del emp_1.fullname

print(emp_1.first, emp_1.last)



# Study Drill :
# 1. Create a Student class,
# attributes (rno, first name, last name, marks)
# methods (display info, email, fullname)
# create an instance of student, print(full_name and email_id)
# First perform without property decorator
# second time with property decorator
