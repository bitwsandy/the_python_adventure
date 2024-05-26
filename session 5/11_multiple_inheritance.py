# Multiple inheritance occurs when a class inherits from more than one base class.
# Care must be taken to manage the complexity and avoid conflicts, such as the diamond problem.

class Father:
    def skills(self):
        print(f"Gardening, Programming")

class Mother:
    def skills(self):
        print("Driving, Art")

class Child(Father, Mother):  # Inherits from both Father and Mother
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")
# self can be used to access methods from parent classes within the child class method. This is
# done by explicitly calling the parent class method with self as the argument, like
# Father.skills(self) and Mother.skills(self). By passing self, you ensure that the
# skills method of the Father and Mother classes is called on the instance of the Child
# class.

# Usage
child = Child()
child.skills()

# Outputs:
# Gardening, Programming
# Cooking, Art
# Sports
