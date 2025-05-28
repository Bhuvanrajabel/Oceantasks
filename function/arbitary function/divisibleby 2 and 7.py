a=int(input("Enter the no:"))
def function(a):
    if (a%2==0) and (a%7==0):
        print("The number is divisible by 2 and 7")
    elif (a%2==0):
        print("The number is divisible by 2")
    elif (a%7==0):
        print("The number is divisible by 7")
    else:
        print("The number is not divisible by 2 or 7")
function(a)
