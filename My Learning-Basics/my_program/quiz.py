print("*** Welcome to the Quiz Program, PLease Enter any key to start.***")
input()
print(" In 1768, Captain James Cook set out to explore which ocean?")
print("A. Pacific Ocean")
print("B. Atlantic Ocean")
print("C. Indian Ocean")
print("C. Indian Ocean")
right_answer = "Pacific Ocean"

choice = (input("Enter your Choice: "))
print("You Entered: ", choice)

if choice == 'A':
    print("Your Answer is Right : ", right_answer)
else:
    print("Sorry, The right Answer was:  ", right_answer)
