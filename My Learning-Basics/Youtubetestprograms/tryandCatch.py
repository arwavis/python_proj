# document https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9061992&gclid=Cj0KCQjw4eaJBhDMARIsANhrQABABr8nGiRFxPKzrlrSjcMDY4QZfIKueGQcwQc5KPODgbGCGlgzTVgaAjREEALw_wcB
# You can also use else in try except method.

try:
    a = 10 / 10
    print(a)
    b = [1, 2, 3]
    print(b[4])
except Exception as e:
    print(e)
finally:
    print("Thank You")

# inbuilt exception list
# exception_list = (dir(locals()['__builtins__']))
# print(exception_list)
# for i in exception_list:
#     print(i)

# multiple exception
try:
    a = 10 / 0
    print(a)
    b = [1, 2, 3]
    print(b[3])

except ZeroDivisionError as e:
    print("Please enter a valid number to divide")

except IndexError as e:
    print("The entered value is out of Index")

else:
    print("No Exception Errors")

finally:
    print("Thank you")

# valuerror

try:
    a = int(input("Enter a number:"))
except  Exception as e:
    print("Only number value is allowed")
else:
    print(a)
finally:
    print("Thank You")

# FileNotFoundError

try:
    f = open("test.txt")
except FileNotFoundError:
    print("File not found")
else:
    print(f.read())
