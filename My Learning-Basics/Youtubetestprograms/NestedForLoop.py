# Nested for loop print *

for i in range (6):
    for j in range(i):
        print( "*", end=" ")
    print(" ")

    # Print * in reverse using for loop

print ("**********************")

for i in range (5,0,-1): # starts with 5 and ends with 0 and each star will be minuses
    for j in range(i):
        print("*", end = " ")
    print("")
