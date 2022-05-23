# We can use Else statement in while loop that helps you print when the loop completes, same is available in for
# Also, if you break the loop then the else statement will not be executed. , Example

i = 1
while i < 6:
    if i == 4:
        break  # I am breaking the loop here so the else statement will not be executed.
    print(i)
    i += 1
else:
    print("The loop is completed")

print("*********************************************")

# Same concept in for loop.

for i in range(5):
    if i == 3:
        break # I am breaking the loop here so the else statement will not be executed.
    print(i)
else:
    print("The loop is complete")
