class Bicycle:
    # Class variables
    num_wheels = 2  # All bicycles typically have 2 wheels
    num_bicycles_created = 0  # Counter for the number of Bicycle instances created

    def __init__(self, make, model):
        # Instance variables
        self.make = make
        self.model = model
        # Increment the class variable using the class name
        Bicycle.num_bicycles_created += 1

    def display_info(self):
        # Accessing class variable using self
        print(f"Make : {self.make} ,Model : {self.model} has {self.num_wheels} wheels.")

# Create instances of Bicycle
bike1 = Bicycle("Trek", "Emonda")
bike2 = Bicycle("Giant", "Defy Advanced")

bike1.num_wheels = 3

# Display information about bike1
bike1.display_info()  # Outputs: Trek Emonda has 2 wheels.
bike2.display_info()

# Display total bicycles created using a class method
print(f"Total bicycles created: {Bicycle.num_bicycles_created}")  # Outputs: Total bicycles created: 2

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
