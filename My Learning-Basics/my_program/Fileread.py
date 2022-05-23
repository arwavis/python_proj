
# To read a file that is in the path /Users/aravindv/Documents/Programming/Python/test.txt
try:
    file_read = open("/Users/aravindv/Documents/Programming/Python/test.txt")
    print(file_read.read())
except FileNotFoundError:
    print(" We are not able to find the file in the location")
finally:
    print("ThankYou")