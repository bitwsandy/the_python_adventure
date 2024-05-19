# Multiple inheritance occurs when a class inherits from more than one base class.
# Care must be taken to manage the complexity and avoid conflicts, such as the diamond problem.

class Father:
    def skills(self):
        print("Gardening, Programming")

class Mother:
    def skills(self):
        print("Cooking, Art")

class Child(Father, Mother):  # Inherits from both Father and Mother
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

# Usage
child = Child()
child.skills()
# Outputs:
# Gardening, Programming
# Cooking, Art
# Sports
