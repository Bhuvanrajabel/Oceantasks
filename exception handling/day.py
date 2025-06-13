def function(day):
    try:
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
    except:
        return "Error"
print(function(2))
