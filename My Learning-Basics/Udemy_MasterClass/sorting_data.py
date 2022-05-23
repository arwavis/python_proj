numbers = [4.5, 2, 1.2, 3, 5, 8.9, 7.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# when you use sorted the original value remains un altered.
# if you use sort that will change the original value. example
numbers.sort()
print(numbers)

# Also you cannot assign numbers.sort to a variable then it will show the result as None . Example

another_sort_number = numbers.sort()
print(another_sort_number)

# How to sort names with differnet case letters.

names = ['raja', 'Girish', 'Murthy', 'gyan', 'praveen']
sorted_names = sorted(names)
print(sorted_names)

# adding case fold
names.sort(key=str.casefold)
print(names)
