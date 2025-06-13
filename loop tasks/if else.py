##program to calculate the grade using given percentage
mark = int(input("Enter the grade:"))
if mark > 90:
    print("S")
elif mark > 80:
    print("A")
elif mark > 70:
    print("B")
elif mark > 60:
    print("C")
elif mark > 50:
    print("D")
elif mark < 40:
    print("F")


##determine the type of triangle using the side length
s = int(input("how many sides are equal:"))
if s == 2:
    print("The triangle is an isosalous triangle")
elif s == 3:
    print("The triangle is an equilateral triangle")
else:
    print("The triangle is an scalen triangle")


##determine the season based on the given month
month = input("Enter the month to find the season:")
if "March" or "April" or "May":
    print("Summer season")
elif "June" or "July" or "August":
    print("Monsoon season")
elif "September" or "october" or "Novmber":
    print("Autumn season")
elif "December" or "January" or "February":
    print("Winter season")

##Minimum salary
x = int(input("Enter the salary of employee x:"))
y = int(input("Enter the salary of employee y:"))
z = int(input("Enter the salary of employee z:"))
if x < y and x < z:
    print("Employee x has the minimum salary")
elif y < x and y < z:
    print("Employee y has the minimum salary")
elif z < x and z < y:
    print("Employee z has the minimum salary")
else:
    print("Salaries of the three employees are same")


 ##leap year or not
year=int(input("Enter the year:"))
if year%4==0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")


##valid triangle
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=a+b+c
if (0<d<=180):
    print("The triangle is valid")
else:
    print("The triangle is invalid")

##Eligiblity for vote
age=int(input("Enter the age:"))
if (age>=18):
    print("eligible for vote")
else:
    print("not eligible for vote")
##vowel or not
letter=input("Enter any letter:")
if letter in "a" or "e" or "i" or "o" or "u":
    print("The letter is a vowels")
else:
    print("The letter is a consonant")

##day of the week
day=int(input("Enter a number:"))
if (day==1):
    print("sunday")
elif (day==2):
    print("monday")
elif (day==3):
    print("tuesday")
elif (day==4):
    print("wednesdy")
elif (day==5):
    print("thursday")
elif (day==6):
    print("friday")
elif (day==7):
    print("saturday")
else:
    print("There is no day")

##Dividible by 5 or 3
d=int(input("Enter the no:"))
if (d%5==0)and (d%3==0):
    print("The number is divisible by 5 and 3")
elif (d%5==0):
    print("The number is divisible by 5")
elif (d%3==0):
    print("The number is divisible by 3")
else:
    print("The number is not divisibl by 5 or 3")

##Check the digit
num=int(input("Enter the number:"))
if(num<100 and num%10==0):
    print("Ones")
elif(100<num<100 and num%100==0):
    print("Twos")
else:
    print("Invalid")
