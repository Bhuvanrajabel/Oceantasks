x = int(input("Enter the salary of employee x:"))
y = int(input("Enter the salary of employee y:"))
z = int(input("Enter the salary of employee z:"))
def function(x, y, z):
    if x < y and x < z:
        print("Employee x has the minimum salary")
    elif y < x and y < z:
        print("Employee y has the minimum salary")
    elif z < x and z < y:
        print("Employee z has the minimum salary")
    else:
        print("Salaries of the three employees are same")
function(x, y, z)
