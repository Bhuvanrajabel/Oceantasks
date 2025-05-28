##Access a string
a = "Vetri"
print(a[3])

b = "Arul"
print(b[2])

c = "Kevin"
print(c[0])

##Find length
d = "Free Fire"
print(len(d))

e = "BGMI"
print(len(e))

f = "COD"
print(len(f))

##loop using string
for i in "Christiano":
    print(i)

for j in "Ronaldo":
    print(j)

for k in "CR7":
    print(k)

##not in
x = "CR7 is the goat"
print("Messi" not in x)

y = "Ramanujam is a teacher"
print("teacher" not in y)

z = "Raistar is a legend"
print("Daddy calling" not in z)

##in
l = "Dhoni is the best captain in the world "
print("captain" in l)

m = "Virat kohli won the cup"
print("lollipop" in m)

n = "Mumbai and Chennai are the best"
print("Chennai" in n)

##slicing a string
a = "Hello"
print(a[2:4])

b = "World"
print(b[1:])

c = "Jerry"
print(c[:3])

##Upper()
d = "Hello"
print(d.upper())

e = "World"
print(e.upper())

f = "Christiano"
print(f.upper())

##lower()
a = "HELLO"
print(a.lower())

b = "WORLD"
print(b.lower())

c = "CHRISTIANO"
print(c.lower())

##Strip()
a = "Hello,World!"
print(a.strip())

b = "Christiano,Ronaldo!"
print(b.strip())

c = "MS,Dhoni!"
print(c.strip())

##Replace a string
a = "Hello"
print(a.replace("H", "h"))

b = "World"
print(b.replace("W", "w"))

c = "Messi"
print(c.replace("M", "p"))

##split
a = "M.S.D"
print(a.split("."))

b = "Hello,World"
print(b.split(","))

c = "OCNSY-17"
print(c.split("-"))
