# set of characters
import re

txt = "The king of the world"
x  = re.findall("[a-h]",txt)

print(x)

# signals
txt="Bhuvan2711 king of BR"
y=re.findall("\d",txt)
print(y)

# any chr
txt="Battlle royal,clash squad"
z=re.findall("Ba....e",txt)
print(z)    

# st with
txt = "battle royal,clash squad"
z = re.findall("^battle",txt)
if z:
    print("The value starts with battle")
else:
    print("false")

# ends with
txt = "battle royal,clash squad"
z = re.findall("squad$", txt)
if z:
    print("The value ends with squad")
else:
    print("no match")

# zero or more occ
txt = "Battle royal,clash squad"
z = re.findall("Ba..*.e", txt)
print(z)

# one or more
txt = "Battle royal,clash squad"
z = re.findall("Ba..+.e", txt)
print(z)

# zero or more
txt = "Battle royal,clash squad"
z = re.findall("Ba..?.e", txt)
print(z)

#
txt = "Battle royal,clash squad"
z = re.findall("Ba.{3}e", txt)
print(z)

# Either or
txt = "battle royal,clash squad"
z = re.findall("Royal|royal", txt)
if z:
    print("The value has the word royal")
else:
    print("false")
