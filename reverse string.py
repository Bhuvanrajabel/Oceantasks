##isalpha()
a="Narenkumar"
print(a.isalpha())

b="Jethro"
print(b.isalpha())

##isupper()
a="HE IS A BOY"
print(a.isupper())

b="CR7 THE GOAT"
print(b.isupper())

##islower()
a="he is a boy"
print(a.islower())

b="cr7 is the goat"
print(b.islower())

##isascii()
a="vincent68"
print(a.isascii())

b="devbts06"
print(a.isascii())

##istitle()
a="Dhoni Is The Best Captain"
print(a.istitle())

b="Virat Kohli Lollipop"
print(b.istitle())

##capitalize()
a="narenkumar"
print(a.capitalize())

b="gnathan"
print(b.capitalize())

##Casefold()
a="Dhoni Is The Best Finisher"
print(a.casefold())

b="Rohit Sharma Hitman"
print(b.casefold())

##Center()
a="Mani"
print(a.center(10))

b="Kohli"
print(b.center(15))

##count()
a="I am the best of the best"
print(a.count("the"))

b= "He is he topper of our class"
print(b.count("topper"))

##endswith()
a="I am the best of them all."
print(a.endswith("."))

b="Who is he ?"
print(b.endswith("?"))

##find()
a= "Kohli is the best player in the world"
print(a.find("player"))

b="tDhoni is a great captain"
print(b.find("is"))

##isspace()
a=" "
print(a.isspace())

b="   "
print(b.isspace())

##lstrip()
a = "     apple     "
b = a.lstrip()
print("in all fruits", b, "is my favorite")

c="    banana   "
d=c.lstrip()
print("out of all ",d, "is my favourite")

##rstrip()

a="   apple   "
b=a.rstrip()
print(" of all",b,"is my favourite")

c="   banana   "
d=c.rstrip()
print(" all of ",d,"is my favourite")

#isdigit()
a="12345"
print(a.isdigit())

#join()
a=("dev","vini","pavi")
print(" and ".join(a))
print(",".join(a))

#startswith()
b="bhuvan23"
print(b.startswith("AI"))
print(b.startswith("123"))

#numeric()
d="444"
print(d.isnumeric())

e="codx"
print(e.isnumeric())

#decimal()
a="123"
print(a.isdecimal())

b="codx"
print(b.isdecimal())

#format
a= " only for {price:.2f} rupees!"
print(a.format(price = 45))
b = "For only {price} dollars!"
print(b.format(price = 10*2))

#LNUM()
a="Python"
print(a.isalnum())

b="c++"
print(b.isalnum())












