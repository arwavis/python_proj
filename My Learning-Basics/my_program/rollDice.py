import random

dice1 = print(random.randint(1, 6))
dice2 = print(random.randint(1, 6))

while dice1 != dice2:
    print(dice1)
    print(dice2)

print("You rolled the doubles")
