# FOR LOOPS EXERCISES

# Ex. 1
# Enter your name, save it in name variable and save in result_1 variable your name repeated 3 times (use loops)
from itertools import repeat

# name_1 = 'eyup'
# for x in range(0, 3):
#     result_1 = name_1
#     print(result_1)

# TODO: Here is your code


# Ex. 2
# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then save in result_2 variable your name repeated as many times as number_1 is
# (use loops)
# name_2 = 'eyup'
# number_1 = 2
# for x in range(0, number_1):
#     result_2 = name_2
#     print(result_2)

# TODO: Here is your code


# Ex. 3
# Enter a random string, which includes only digits. Write code which find a sum of digits in this string and save it
# into result_3 variable

# string_number_1 = 1234
# result_3 = 0
# for val in str(string_number_1):
#     result_3 = result_3 + int(val)
# print(result_3)

# TODO: Here is your code


# Ex. 4
# Create code which sums up all even numbers between 2 and 100 (include 100) and save it in result_4 variable

result_4 = 0
for number in range(2, 101):
    if number % 2 == 0:
        result_4 = result_4 + number
print(result_4)

# TODO: Here is your code
