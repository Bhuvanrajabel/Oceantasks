# input=[12,13,4,5,87,90]
# def even_number(numbers):
#     even_number=[]
#     for num in numbers:
#         if num%2==0:
#             even_number.append(num)
#     print(even_number)
# even_number(input)

# file handling
# a = input("Enter name1:")
# b = input("Enter name2:")
# c = input("Enter name3:")
# with open("name.txt", "w") as file:
#     file.write(a + "\n")
#     file.write(b + "\n")
#     file.write(c + "\n")
# with open("name.txt", "r") as file:
#     for name in file:
#         print(name.strip().upper())

#exceptional handling
# try:
#     a=float(input("Enter the number:"))
#     b=float(input("Enter the number:"))

#     c=a/b
#     print(c)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("invalid number")

#class and bject
# class Rectangle:
#     def __init__ (self,length,width):
#         self.length=length
#         self.width=width

#     def area(self):
#         return self.length*self.width
# rect = Rectangle (20,5)
# print(rect.area())

#Dictionaries
students_mark={
    "dev":90,
    "kishanth":98,
    "nathan":100
    }

print("Students marl dictionary:")
print(students_mark)

average=sum(students_mark.values())/len(students_mark)
print(f"\n Average Mark: {average:.2f}")
