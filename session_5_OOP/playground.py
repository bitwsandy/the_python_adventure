
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
car1.print_details()







