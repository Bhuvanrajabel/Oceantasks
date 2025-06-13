#print all numbers from 1 to 15
for i in range (1,16):
   print (i)


#print odd numbers from 6 to 29
for j in range (7,30,2):
   print(j)


##print even numbers from 20 to 40
for k in range (20,40,2):
   print (k)


##iterate through all numbers from 1 to 15
for l in range (1,16):
   if l%3==0:
       print(l)

for m in range (1,16):
   if m%5==0:
       print(m)

for n in range (1,16):
   if n%3==0 and n%5==0:
       print (n)

##print all elements in the list
mylist=[2,12,22,32,42]
print(mylist)

##calculate sum of all elements in a list
list=[5,10,15,20]
sum=0
for i in list:
   sum+=i
print(sum)


#calculate the sum of all numbers  from 1 to 100
s=0
for i in range (1,101):
   s+=i
   print(s)

##calculate the factorial of a given number
num=int(input("Enter a number:"))
s=1
for i in range(1,num+1):
   s*=i
   print(s)
