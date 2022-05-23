"""
If Pass Grade
90-100      A
80-89       B
70-79       C
Else          D

"""
m1 = int(input("Enter the Mark for subject Science: "))
m2 = int(input("Enter the Mark for subject English: "))
m3 = int(input("Enter the Mark for subject Maths: "))

total = m1 + m2 + m3
average = total / 3
print("Total: ", total)
print("Average: ", average)

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("You have passed the Exam")
    if average >= 90 and average <= 100:
        print("You have aced with a grade:  A")
    elif average >= 80 and average <= 89:
        print("Grade B")
    elif average >= 70 and average <= 79:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Sorry, you have failed the Exam")
    print("No Grade")
