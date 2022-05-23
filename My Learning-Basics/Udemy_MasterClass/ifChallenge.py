name = input("Enter your name: ")
age = int(input("Enter your age: "))

# if 18 <= age < 31:
if age >= 18 and age <31:
    print("Hello ", name, "Welcome to the holiday, Have fun !")
elif age < 18:
    print("Hello ", name, "Sorry you are not yet ready, Please come after {0}, years".format(18 - age))
else:
    print("Hello ", name, "You are too old to party here.")
