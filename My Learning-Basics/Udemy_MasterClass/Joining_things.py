flowers = ["Rose", "Lilly", "Daffodil", "Blue Rose"]

# normal way of printing the list

for flower in flowers:
    print(flower)

# using join methid to print the same

separator = " > "
output = separator.join(flowers)
print(output)

# or

print (", ".join(flowers))