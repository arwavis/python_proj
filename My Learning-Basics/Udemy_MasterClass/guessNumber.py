import random

number = 10
answer = random.randint(1, number)
print(answer)  # TODO: Delete this later
guess = 0
print("Please guess  a value between 1 and {}: ".format(number))

count = 1
while guess != answer:
    guess = int(input())

    if guess == 0 or guess > number:
        print("Please input the number between 1 to {} ".format(number))
        break

    if guess == answer:
        print("Well done you have guessed it correct")
        if count == 1:
            print("Great you have guessed the answer in First Guess ")
        else:
            print("Great you have guessed the answer in {} guess".format(count))
        break

    else:
        if guess < answer:
            print("Please guess higher")
            count = count + 1
        else:
            print("Please guess lower")
            count = count + 1
