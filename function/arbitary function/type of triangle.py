a=int(input("Enter the side length:"))
b=int(input("Enter the side length:"))
c=int(input("Enter the side length:"))
def function(a,b,c):
    if a==b==c:
        print("The triangle is an equilateral triangle")
    elif b==c or a==c or a==b:
        print("The triangle is an  isosalous  triangle")
    else:
        print("The triangle is an scalen triangle")
function(a,b,c)