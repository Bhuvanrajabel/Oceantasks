# difference()
x={"Rajesh","Sekar","Shankar"}
y={"Android","Shankar","Kumar"}
z=x.difference(y)
print(z)

x = {"Android", "Shankar", "Kumar"}
y = {"Rajesh", "Sekar", "Shankar"}
z = x.difference(y)
print(z)

# Difference_update()
x = {"Rajesh", "Sekar", "Shankar"}
y = {"Android", "Shankar", "Kumar"}
x.difference_update(y)
print(x)


x = {"Android", "Shankar", "Kumar"}
y = {"Rajesh", "Sekar", "Shankar"}
x.difference_update(y)
print(x)

# issubset()
a={"a","b","c","d"}
b={"g","f","e","d","c","b","a"}
c=a.issubset(b)
print(c)

b= {"g", "f", "e", "d", "c", "b", "a"}
a = {"a", "b", "c", "d"}
c = a.issubset(b)
print(c)

# issuperset()
a = {"g", "f", "e", "d", "c", "b", "a"}
b = {"a", "b", "c", "d"}
c = a.issuperset(b)
print(c)

# symmetricdifference
a={"Oppo","Vivo","Samsung"}
b={"Poco","Vivo","Apple"}
c=a.symmetric_difference(b)
print(c)

# symmetric difference update
a = {"Oppo", "Vivo", "Samsung"}
b = {"Poco", "Vivo", "Apple"}
a.symmetric_difference_update(b)
print(a)

# Intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
z = y.intersection(x)
print(z)

# Intersection Update
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
y.intersection_update(x)
print(y)
