import random


def ran():
    random_number = random.randint(1000, 10000)
    return random_number


for i in range(4):
    print(ran())
