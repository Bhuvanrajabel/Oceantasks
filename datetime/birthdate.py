#birth day
import datetime
birth=int(input("Enter a year:"))
x=datetime.datetime.now()
print(x)
print(x.year)
year=x.year
if birth>year:
    print("invalid")
age=year-birth
print(age)