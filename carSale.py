print("Welcome to Car Dealership :)")
print("*" * 80)

car = input("Please tell us if you are here to buy a car or sell a car : Enter 'buy' or 'sell':  ")


def buy():
    """
    This function is used when users select to buy a car.
    """
    budget = (int(input("What is your budget? :")))
    if budget > 10000:
        print("Great, A nissan Ultima is available")

    valid_insurance = input("Do you have Insurance? Write 'Yes' or 'No' :")
    valid_license = input("Do you have a valid license? Write 'Yes' or 'No' :")
    credit_score = int(input("What is your Credit Score? : "))

# Using casefold() will accept user input in any case of letters (Lower or Upper case)

    if valid_license.casefold() == "yes" and valid_insurance.casefold() == "yes" and credit_score > 600:
        print("Sold, Pleasure doing business with you")
    else:
        print("Sorry You are not eligible.")
    exit(0)


def sell():
    """
    This function is used when users select to sell a car.
    """
    car_value = int(input("What is your car valued at? : "))
    car_price = int(input("What is your selling price? :"))

    if car_value > car_price and car_price < 30000:
        print("We will buy your car, Pleasure doing business with you")
    else:
        print("Sorry, We are not interested")
    exit(0)


def other():
    """
    This function is used when users select a wrong choice.
    """
    second_chance = input("Please tell us if you are here to buy a car or sell a car : Enter 'buy' or "
                          "'sell':  ")
    if second_chance.casefold() == 'buy':
        buy()
    elif second_chance.casefold() == 'sell':
        sell()
    else:
        print("Sorry, We are wasting our time.")


if car.casefold() == str("buy"):
    buy()
elif car.casefold() == str("sell"):
    sell()
else:
    while car.casefold() != "buy" and car.casefold() != "sell":
        other()
