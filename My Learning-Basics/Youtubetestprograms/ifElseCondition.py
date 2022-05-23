# Write a program to check eligibility by enter his/her name and age

name = input("Enter a Name: ")
age = int(input("Enter a age: "))

if age >= 18:
    print(name,  " is ", age, " years old, and eligible for voting")
else:
    print(name,   " is ", age, " years old, and not eligible for voting ")
