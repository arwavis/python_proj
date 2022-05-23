# This program helps you find the index where your item is present.

shopping_list = ["Milk", "Bread", "Eggs", "Rice", "Flour", "Cake"]

item_to_find = "Oats"
found_at = None  # None is  constant used to say there is no value.

# for index in range(len(shopping_list)):  # This is will iterate the index in the list
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break  # So rest of the items in the list will not be processed, once the item is found the loop will break

# You can write the above code as below
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at index: ", found_at)
else:
    print("Item not found in the list")