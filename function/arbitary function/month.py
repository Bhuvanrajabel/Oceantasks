month = input("Enter the month to find the season:")
def function(month):
    if month in ("March", "April" , "May"):
        print("Summer season")
    elif month in  ("June" ,"July" , "August"):
        print("Monsoon season")
    elif month in  ("September" , "October" , "Novmber"):
        print("Autumn season")
    elif month in ("December" , "January" , "February"):
        print("Winter season")
    else:
        print("not a valid month")
function(month)
