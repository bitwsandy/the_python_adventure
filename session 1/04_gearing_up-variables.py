cars = 100
# print("Cars Data Type : ", type(cars))
space_in_a_car = 4.0
# print("space_in_a_car Data Type : ", type(space_in_a_car))
drivers = 30
# print(type(drivers))
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")