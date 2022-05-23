import datetime as dt

# You can set a alias for the package you import and you can use that alias name in the program, For example

current_date = dt.date.today()
print(current_date)

# To create a new date

new = dt.date(2021, 5, 5)
print(new)

# You can also print date , month and time separately

print("Year : ", current_date.year)
print("Month : ", current_date.month)
print("Day :", current_date.day)

print("*" * 80)
# To print Date and time

time = dt.datetime.now()
print(time)

print("Year : ", current_date.year)
print("Month : ", current_date.month)
print("Day :", current_date.day)
print("Hour : ", time.hour)
print("Minute : ", time.minute)
print("second :", time.second)
print("Micro Second", time.microsecond)

print("*" * 80)
# how to set date and time manually

new_time = dt.datetime(2022, 5, 30, 11, 30, 56, 55556)
print(new_time)
print("*" * 80)

# Time difference
current_date = dt.datetime.now()
new_year = dt.datetime(2022, 1, 1)
difference = new_year - current_date

print("No of days to New Year: ", difference)

s = current_date.strftime("%A %b %d %Y")
print(s)
