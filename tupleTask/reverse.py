x = ("Raju", 56, 34.2, True, [1, 2, 3])
print(x)

x = (23, 45, 6, 90)
y = x[3]
print(y)

x = (1, 2, 3, 4, 5, 6)
y = x[-5:]
print(y)


a = (1, 2, 3)
b = (4, 5, 6)
result = a + b
print(result)

x = (1, 2, 3)
y = x * 3
print(y)

x = (1, 2, 3, 4, 5)
if 4 in x:
    print("4 exists in the tuple")
else:
    print("4 does not exist in the tuple")

a = (10, 20, 30, 40)
b = len(a)
print(b)


x = (1, 2, 3)
y = list(x)
y[1] = 20
z = tuple(y)
print(z)

my_tuple = (10, 20, 30, 40)
index = my_tuple.index(30)
print(index)

a = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = a.count(5)
print(x)

