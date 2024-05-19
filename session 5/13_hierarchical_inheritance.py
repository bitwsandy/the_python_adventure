# Hierarchical inheritance involves multiple classes inheriting from a single base class.

class Vehicle:
    def general_usage(self):
        print("General use: Transportation")

class Car(Vehicle):  # Inherits from Vehicle
    def specific_usage(self):
        print("Specific use: Drive to work")

class Truck(Vehicle):  # Inherits from Vehicle
    def specific_usage(self):
        print("Specific use: Transport goods")

# Usage
car = Car()
truck = Truck()
car.general_usage()  # Outputs: General use: Transportation
car.specific_usage()  # Outputs: Specific use: Drive to work
truck.general_usage()  # Outputs: General use: Transportation
truck.specific_usage()  # Outputs: Specific use: Transport goods
