# Total available cars
cars = 100
# Available space in each car
space_in_a_car = 4.0
# Total available drivers
drivers = 30
# Total available passengers
passengers = 90
# Number of cars not driven
cars_not_driven = cars - drivers
# Number of cars driven
cars_driven = drivers
# Calculate carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculate average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are",cars,"cars available.")
print("There are only",drivers,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today")
print("We need to put about", average_passengers_per_car,"in each car.")
