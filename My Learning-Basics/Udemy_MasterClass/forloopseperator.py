number = "922,;345;456;;,678 785 , 876"
seperator = " "

for char in number:
    if not char.isalnum():
        seperator = seperator + char

print(seperator)

values = " " .join(
    char if char not in seperator else " " for char in number).split()
print([int(val) for val in values])
