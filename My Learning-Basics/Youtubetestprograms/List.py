# This is similar to an array in other languages
# However, in Python you can store any values  in the list and the list is mutable.

a = [2, 3, 4, 5, 6, 7, 8]
print(a)  # prints the complete list
print(type(a))  # Prints the type of list
a[0] = 100  # update the Index 0 from 2 to 100
print(a)
print(a[0])  # prints the first index of list if you want the second inex then
print((a[1]))
print(a[-1])  # I can print the negative digit too and this will print last digit of the list.,
print("Slicing in List")
print(a[0:3])  # Will print the range in the list
print(a[3:])
print(a[:4])

# In python List you can store any values

b = [2, True, "Ram", 3.5, [3, 4, 6, 7]]
print(type(b))
print(b[0], "is a", type(b[0]))
print(b[1], "is a", type(b[1]))
print(b[2], "is a", type(b[2]))
print(b[3], "is a", type(b[3]))
print(b[4], "is a", type(b[4]))

# To get  value for inner list
print(b[4][2])
