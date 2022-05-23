# This programs excludes the item that you marked in "items_to_be_excluded" and prints the rest.

items = ["Milk", "Bread", "Eggs", "Rice", "Flour"]
# print(type(items))

items_to_be_excluded = "Eggs"
item_no = None

for i in items:
    if i == items_to_be_excluded:
        continue

    print ("Buy " + i)