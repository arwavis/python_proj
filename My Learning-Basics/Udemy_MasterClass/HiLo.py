low = 1
high = 1000

print("Please think a number between {0} and {1}".format(low, high))
input("Press Enter to Start⎆")

guesses = 1

while True:
    print("\tGuessing in the range of {0} to {1}".format(low, high))
    guess = low + (high - low) // 2
    #print(guesses)
    high_low = input(
        "My guess is {}. Should i guess Higher or Lower? Enter h or l or c if my guess was correct:  ".format(
            guess)).casefold()
    if high_low == "h":
        # Guess Higher, The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess Lower, high end of the range becomes 1 lesser than the guess
        high = guess - 1
    elif high_low == "c":
        print("I got the answer in {} guess".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    guesses = guesses + 1
