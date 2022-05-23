available_parts = ["Computer", "Monitor", "HDMI Cable", "Mouse", "KeyBoard", "Mouse Pad"]
# Comprehension
# valid_choices= [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = '-'
computer_parts = []

while current_choice != '0':
    #    if current_choice in "123456":
    # Change the abe code to
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    # Replacng the below if elif command with the above code
    # if current_choice == "1":
    #     computer_parts.append("Computer")
    # elif current_choice == "2":
    #     computer_parts.append("Monitor")
    # elif current_choice == "3":
    #     computer_parts.append("HDMI Cable")
    # elif current_choice == "4":
    #     computer_parts.append("Mouse")
    # elif current_choice == "5":
    #     computer_parts.append("Keyboard")
    # elif current_choice == "6":
    #     computer_parts.append("Mouse Pad")
    else:
        print("PLease add the options from the list below:")
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))
        # You can also write the above code using enumerate method
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
print("Recorded Computer Parts are : ", computer_parts)
