import numpy as np

# Simulated temperature data (in degrees Celsius) for one week
# Each row represents a day, and each column represents a different city
temperature_data = np.array([
    [22.1, 23.4, 21.7, 24.5],
    [22.5, 23.8, 21.1, 24.8],
    [21.7, 23.3, 20.9, 24.2],
    [22.6, 23.5, 21.8, 24.9],
    [22.1, 23.6, 21.2, 24.4],
    [21.9, 23.4, 21.5, 24.5],
    [22.2, 23.5, 21.7, 24.6]
])

# Calculating basic statistics for the dataset

# Mean temperature for each city
mean_temperatures = np.mean(temperature_data, axis=0)
print("Mean temperatures for each city:", mean_temperatures)

# Minimum and maximum temperatures for the dataset
min_temperature = np.min(temperature_data)
max_temperature = np.max(temperature_data)
print("Minimum temperature recorded during the week:", min_temperature)
print("Maximum temperature recorded during the week:", max_temperature)

# Standard deviation of temperatures for each city
std_deviation = np.std(temperature_data, axis=0)
print("Standard deviation of temperatures for each city:", std_deviation)

# Identify days with above average temperatures for the first city
first_city_temperatures = temperature_data[:, 0]
above_average_days = np.where(first_city_temperatures > np.mean(first_city_temperatures))
print("Days with above average temperatures for the first city:", above_average_days)

# Example of applying a function - Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

fahrenheit_temperatures = celsius_to_fahrenheit(temperature_data)
print("Temperature data in Fahrenheit:\n", fahrenheit_temperatures)

# Visualizing the data for better understanding (Optional, requires matplotlib)
# Uncomment the following lines if you wish to visualize the data
# import matplotlib.pyplot as plt
# plt.plot(temperature_data)
# plt.title('Daily Temperature Readings Across Four Cities')
# plt.xlabel('Day of the Week')
# plt.ylabel('Temperature (Celsius)')
# plt.legend(['City 1', 'City 2', 'City 3', 'City 4'])
# plt.show()

