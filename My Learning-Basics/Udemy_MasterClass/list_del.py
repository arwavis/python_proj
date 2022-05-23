data = [104, 203, 156, 4, 6, 890, 112, 121, 125, 167, 189, 360,1045]

# Writing a program to delete all the values less than 100 and greater than 200
min_value = 100
max_value = 200

# method 1:

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min_value or data[index]>max_value:
#        # print(index, data)
#         del data[index]
#
# print(data)

# method 2 using reversed.
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
