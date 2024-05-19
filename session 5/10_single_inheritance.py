# In single inheritance, a child class inherits from one parent class. This is
# a straightforward and easy-to-understand form of inheritance.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

# Usage
dog = Dog()
dog.speak()  # Outputs: Animal speaks
dog.bark()   # Outputs: Dog barks
