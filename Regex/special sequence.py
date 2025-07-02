import re
txt = "battle royal,clash squad"
z = re.findall("\d", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")

#
txt = "battle royal,clash squad"
z = re.findall("\D", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")

#
txt = "battle royal,clash squad"
z = re.findall("\s", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")


#
txt = "battle royal,clash squad"
z = re.findall("\S", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")

#
txt = "battle royal,clash squad"
z = re.findall("\w", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")

#
txt = "battle royal,clash squad"
z = re.findall("\W", txt)
print(z)
if z:
    print("The value starts with battle")
else:
    print("false")
