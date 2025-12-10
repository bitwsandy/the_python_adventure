
cars = 100
drivers = 30
single_car_capacity = 4
passengers = 100

total_cars = cars
cars_driven = drivers
cars_not_driven = cars - drivers
total_capacity = cars * single_car_capacity
capacity_today = cars_driven * single_car_capacity
avg_passengers_per_car = capacity_today / passengers


# Comma
print("Total Cars :", total_cars)
# Format String
print(f"Total Cars : {total_cars}")
# Format Function
print("Total Cars : {}".format(total_cars))


# Comma
print("Total Cars :", total_cars, "Good Day")
# Format String
print(f"Total Cars : {total_cars} Good Day")
# Format Function
print("Total Cars : {} Good Day".format(total_cars))


print(f"Cars Driven : {cars_driven}")
print(f"cars not driven : {cars_not_driven}")
print(f"Total Capacity {total_capacity}")
print(f"Today's Capacity {capacity_today}")
print(f"Average Passengers Per Car {avg_passengers_per_car}")




