from _typeshed import IdentityFunction
import random
from turtledemo.chaos import f

myFirstString = "Today is Friday"
print(myFirstString)

# for any special characters in a string that has 's can be fixed by adding a \ known as escape key.
firstSplitString = "Today is \nFriday and \nit\'s a \nWeekend"
print(firstSplitString)

# or you can also use three *'s for any special characters like this.

specialString = """ My friend Said he is on a Vacation. He requested not to be disturbed 'e 's I'am ok with that.   """
print(specialString)


n = random.randint(0, 22)
print(n)

slice_test = "abcdefghijklmnopqrstuvwxyz"

print(slice_test[1:4])
print(slice_test[4:])
print(slice_test[-15:])
print(slice_test[:15])

# using format to complete a sentence.

print("This month has {0} days in total {1} months".format(31, 12))

# for loop

for i in range(1, 12):
    print(i, " ")

    # square and cube
    for i in range(1, 13):
        print("The No {0:2} ,  square root is {1:6}  and the cube is {2:6} ".format(
            i, i ** 2, i ** 3))

# Arithmetic calculation
a = 12
b = 15
c = a + b
print("Total is :", c)
print(" I'm starting my career in Python from today")

# using f string does not work for me instead using , to add a string and number

age = 24
name = "raj"

print(name + " is", age, "years old")

# Arrays or called Lits in Python

para = [24, 56, 43]
print(type(para))
print((para[2]))

# Another Example to input a para

paragraph = []
print(type(paragraph))
print("Enter a Paragraph:  ")

while True:
    line = input()
    if line:
        paragraph.append(line)
    else:
        break

print(paragraph)
