# Print even numbers using for loop

for i in range(0, 21, 2):
    print(i, end=" ")  # Using End you can print the for statement in the single line

# Print odd numbers using for loop
print("\n------------------------------------")

for i in range(1, 20, 2):
    print(i, end=" ")

print("\n------------------------------------")


# # print following using for loop
# ABCDE
# ABCDE
# ABCDE
# ABCDE
# ABCDE

for i in range(65, 70, 1):
    for j in range(65, 70, 1):
        print(chr(j), end=" ")
    print(" ")
