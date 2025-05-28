x={
    "Name" : "Christiano",
    "Age" : "41",
    "Mobile" :"6532145263"
}
print(x)
print(type(x))
print(len(x))
print(type(x["Name"]))

x = { 
    "Name": "Christiano",
    "Age": "41",
    "Mobile":"6532145263",
    "Age": "23"
}
print(x)
print(x["Name"])
print(x.keys())
print(x.values())
print(x.items())


x= { 
    "Name": "Christiano",
    "Age": "41",
    "Mobile":"6532145263",
}
if "Age" in x:
    print("Yes, 'Age' is in x")

y={
    "name":"Dhoni",
    "Role":"Finisher",
    "Team":"CSK"
}
y.update({"Team":"India"})
print(y)
y["Team"]="India"
print(y)

y = {
    "name": "Dhoni",
    "Role": "Finisher", 
    "Team": "CSK"
}
'''y.update({"Best":"187"})
print(y)
x.popitem()
print(y)'''

y.pop("Role")
print(y)

y.clear()
print(y)

mydict=y.copy()
print(mydict)

