##leap year or not
year = int(input("Enter the year:"))
if year % 4 == 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


##valid triangle
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
d = a + b + c
if 0 < d <= 180:
    print("The triangle is valid")
else:
    print("The triangle is invalid")

##Eligiblity for vote
age = int(input("Enter the age:"))
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")
##vowel or not
letter = input("Enter any letter:")
if letter in "a" or "e" or "i" or "o" or "u":
    print("The letter is a vowels")
else:
    print("The letter is a consonant")

##day of the week
day = int(input("Enter a number:"))
if day == 1:
    print("sunday")
elif day == 2:
    print("monday")
elif day == 3:
    print("tuesday")
elif day == 4:
    print("wednesdy")
elif day == 5:
    print("thursday")
elif day == 6:
    print("friday")
elif day == 7:
    print("saturday")
else:
    print("There is no day")

##Dividible by 5 or 3
d = int(input("Enter the no:"))
if (d % 5 == 0) and (d % 3 == 0):
    print("The number is divisible by 5 and 3")
elif d % 5 == 0:
    print("The number is divisible by 5")
elif d % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisibl by 5 or 3")

##Check the digit
num = int(input("Enter the number:"))
if num < 100 and num % 10 == 0:
    print("Ones")
elif 100 < num < 100 and num % 100 == 0:
    print("Twos")
else:
    print("Invalid")
