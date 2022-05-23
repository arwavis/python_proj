import itertools
import random

# Password Generator - To not repeating the character used Set method

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

no_of_digits = int(input("Enter the number of digits you need in your password: "))
no_of_lowcase = int(input("Enter the number of lower case characters you need in your password: "))
no_of_uppercase = int(input("Enter the number of upper case characters you need in your password: "))
no_of_symbols = int(input("Enter the number of symbols you need in your password: "))

password_list = []
for digit in range(1, no_of_digits + 1):
    # set is used so the digits will not be repeated
    password_list.append(set(random.choice(DIGITS)))

for lower in range(1, no_of_lowcase + 1):
    # set is used so the lower case character will not be repeated
    password_list.append(set(random.choice(LOCASE_CHARACTERS)))

for upper in range(1, no_of_uppercase + 1):
    # set is used so the Upper case character will not be repeated
    password_list.append(set(random.choice(UPCASE_CHARACTERS)))

for symbol in range(1, no_of_symbols + 1):
    # set is used so the symbols will not be repeated
    password_list.append(set(random.choice(SYMBOLS)))

# print(password_list)
# This will shuffle the Password List
random.shuffle(password_list)
# print(password_list)

# Here the output will be in set, so we are converting the set to list.
convert_list = []
for char in password_list:
    s = list(char)
    convert_list.append(s)
# print(convert_list)

# The below code helps you concatenate separate list to a single list.
list_concat = list(itertools.chain.from_iterable(convert_list))

# Finally, we are converting the list to a String
password = ""

for char in list_concat:
    password += char

print(password)
