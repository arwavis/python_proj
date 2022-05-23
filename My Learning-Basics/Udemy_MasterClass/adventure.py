available_exits = ["North", "South", "East", "West"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please chose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
print("Aren't you glad you got out of there")

"""
Test Message 
"""
