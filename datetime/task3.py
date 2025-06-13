import datetime
birthday = int(input("Enter a day: "))
birthmonth = int(input("Enter a month: "))
birthyear = int(input("Enter a year: "))
birth_days = datetime.datetime(birthyear, birthmonth, birthday)
x = datetime.datetime.now()
dayslived = (x - birth_days).days
print("You have been lived for", dayslived, "days")
 