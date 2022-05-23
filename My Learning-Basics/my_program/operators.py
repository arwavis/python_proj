input_number_one = int(input("Please enter a First number: "))
input_number_two = int(input("Please enter a Second number: "))

print("Available choices: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. divide")
print("5. Modules")

input_choice = int(input("Chose your selection from 1 to 5: "))
print("You selected : ", input_choice)


def add(first, second):
    """
    This function is used to add given two numbers
    """
    addition = first + second
    print("Additional value of First and Second number is:", addition)


def sub(first, second):
    """
    This function helps subtracts the given two numbers
    """
    subtract = first - second
    print("Subtract value of First and Second number is:", subtract)


def mul(first, second):
    """
    This function helps multiply the give two numbers
    """
    multiply = first * second
    print("The Multiplied value of First and Second number is: ", multiply)


def div(first, second):
    """
    This function helps divide the give two numbers
    """
    divide = first / second
    print("The Division of First and Second Number is: ", divide)


def mod(first, second):
    """
    This function helps find the reminder in the give two numbers
    """
    modules = first % second
    print("The Modules of First and Second number is: ", modules)


if input_choice == 1:
    add(input_number_one, input_number_two)
elif input_choice == 2:
    sub(input_number_one, input_number_two)
elif input_choice == 3:
    mul(input_number_one, input_number_two)
elif input_choice == 4:
    div(input_number_one, input_number_two)
elif input_choice == 5:
    mod(input_number_one, input_number_two)
else:
    print("The choice you entered is not in the list")
