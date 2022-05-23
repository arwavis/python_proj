file_to_write = open("/Users/aravindv/Documents/Programming/Python/test.txt", mode="w", encoding="utf-8")
count = 1
file_to_write.write("1. Writing to a new file\n")
file_to_write.write("2. Writing to a new file\n")
file_to_write.write("3. Writing to a new file\n")

# Append to the existing file

file_to_write.close()