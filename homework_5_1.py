# FUNCTIONS

# Difference
# Write a function, which will calculate the difference of these two numbers
num_1 = 3
num_2 = 4


def difference(num_1, num_2):
    return num_1 - num_2


print(difference(num_1, num_2))


# Division
# Write a function, which will divide these two numbers

def division(num_1, num_2):
    return num_1 / num_2
    pass


print(division(num_1, num_2))

# Function gets random number. If this number is more than ten, return the difference between 100 and this number,
# otherwise return this number multiplied by 10
number = 11


def function_1(number):
    if number < 10:
        return 100 - number
    else:
        return 10 * number
    pass


print(function_1(number))

# Your function temerature_convertor gets the temperature in Fahrenheit, convert it to Celsius and return.
# Formula (32°F − 32) × 5/9 = 0°C
fahrenheit_degree = 80


def temperature_convertor(fahrenheit_degree):
    return (fahrenheit_degree - 32) * (5 / 9)
    pass


print(temperature_convertor(fahrenheit_degree))

# Taxi Fare
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for every 140 meters travelled.
# Write a function that takes the distance travelled (in kilometers) as its only parameter and returns the total fare
# as its only result rounded by 2 digits. Write a program that demonstrates the function.
distance = 10
base_fare = 4
fare = 0.25


def taxi_fare(distance):
    return round((distance * 1000 / 140 * fare + base_fare), 2)
    pass


print(taxi_fare(distance))

# examples of usage:
# taxi_fare(10) #21.86
