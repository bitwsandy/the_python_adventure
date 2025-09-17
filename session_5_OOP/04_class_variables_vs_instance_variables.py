class Car :
    num_wheels = 4
    def __init__(self, name, make, color, mileage):
        self.name = name
        self.make = make
        self.color = color
        self.mileage = mileage

    def print_details(self):
        print(self.name, self.make, self.color, self.mileage)


car1 = Car("Tiago", "TATA", "Orange", 20)
# __init__(car1, "Tiago", "TATA", "Orange", 20 )

car2 = Car("Alto", "MS", "While", 20)


# # Accessing class variable using instance and class
# print(car1.num_wheels)
# print(car2.num_wheels)
# print(Car.num_wheels)

# # Accessing Instance variable using instance and class
# print(car1.name)
# print(car2.name)
# # print(Car.name) # Instance variables cannot be accessed using Class

# # Modify class variable using instance and class
# car1.num_wheels = 8
# print(car1.num_wheels)
# print(car2.num_wheels)
# print(Car.num_wheels)

# # Modify class variable using instance and class
# Car.num_wheels = 8
# print(car1.num_wheels)
# print(car2.num_wheels)
# print(Car.num_wheels)

# Modify Instance variable using instance
car1.print_details()
car1.name = "TiagoXZ"
car1.print_details() # Outputs: Total bicycles created: 2

# Class variables : Variables that are shared among all instances (objects) of a class.
# They are defined within the class definition but outside of any instance methods.
# Any change made to a class variable affects all instances of that class.
#
# Instance variables : Variables that are unique to each instance of a
# class. They are defined inside the constructor method (__init__) using the self keyword.
# Each instance of the class can have different values for its instance variables.
#
# In short: Class variables are shared by all instances of a class, while instance variables
# are unique to each instance.


# Study Drills :
# 1. Try to get num_of_wheels using instance and class.
# 2. Try to get value for num_of_wheels using self and class name inside a class method
# 3. Print all contents of Class and instances using __dict__
# 4. Try to Change value for class variable through instance and class and figure out the difference

