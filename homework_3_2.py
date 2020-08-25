# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write code, which will count how many times your character is included in your string.
# Save result to result_1 variable

# string_1 = 'random'
# char_1 = 'a'
# result_1 = string_1.count(char_1)
# print(result_1)

# Enter a random number and save it in variable number_1. Then create code to  multiply all the digits together
# and save result in the result_2 variable.

number_1 = 12342
result_2 = 1

for number in str(number_1):
    result_2 = result_2 * int(number)
print(result_2)

# Enter a random number and save it in variable number_2. Then create code which will return
# a number with digits of number_1 in reverse order. Save it in result_3 variable

number_2 = 1234
string_2 = str(number_2)
result_3 = (string_2[::-1])
print(result_3)
