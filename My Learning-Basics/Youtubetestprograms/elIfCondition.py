"""
Write a program to return a book and fine accordingly as below if delayed.

0           No fine
1-5        0.5
5-10        1
10-30     5
>30         Membership Cancel
"""

days = int(input("Enter the number of days: "))

if days == 0:
    print("Thank You, No Fine as you returned the book on time")
elif days >= 1 and days <= 5:
    print("you have delayed the return by ", days,
          " days and the fine is ", days * 0.5, "$")
elif days > 5 and days <= 10:
    print("you have delayed the return by ", days,
          " days and the fine is ", days * 1, "$")
elif days > 10 and days <= 30:
    print("you have delayed the return by ", days,
          " days and the fine is ", days * 5, "$")
else:
    print(" Since you have delayed by ", days,
          " days. We are sorry and we have to cancel your subscription")
