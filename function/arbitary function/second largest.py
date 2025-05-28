a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
def function(a,b,c):
    if (a>b and a<c) or (a>c and a<b):
        print(a)
    elif (b>a and b<c) or (b>c and b<a):
        print(b)
    else:
        print(c)
function(a,b,c)
