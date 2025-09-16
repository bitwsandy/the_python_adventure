
class Car :
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

# car1.print_details()
Car.print_details(car1)

car2.print_details()










