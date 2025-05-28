mark = int(input("Enter the grade:"))
def function(mark):
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
function(mark)
