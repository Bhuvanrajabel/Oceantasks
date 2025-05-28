a = {"Kumar", "Ravi", "Rahul"}
print(a)
print(tuple(a))
print(len(a))

b = {"Ravi", 123345, True, "Kannan"}
print(b)
print(tuple(b))
print(len(b))

c = {"Kumar", "Ravi", "Rahul"}
for x in c:
    print(x)

d = {"Ravi", 123345, True, "Kannan"}
for y in d:
    print(y)

a = {"Kumar", "Ravi", "Rahul"}
print("Kumar" in a)
print("sekar" in  a)

b = {"Ravi", 123345, True, "Kannan"}
print("Ravi" in b)
print("Dog" in b)

a = {"Kumar", "Ravi", "Rahul"}
a.add("Rohit")
print(a)

b = {"Ravi", 123345, True, "Kannan"}
a.add("Kohli")
print(b)

x = {"apple", "banana", "cherry"}
tropical = { "mango", "papaya"}
x.update(tropical)
print(x)

x= {"apple", "banana", "cherry"}
y=["Orange","Purple"]
x.update(y)
print(x)

x = {"apple", "banana", "cherry"}
x.remove("banana")
print(x)

x = {"apple", "banana", "cherry"}
x.discard("banana")
print(x)

a = {"apple", "banana", "cherry"}
x = a.pop()
print(x)
print(a)

x = {"apple", "banana", "cherry"}
x.clear()
print(x)
