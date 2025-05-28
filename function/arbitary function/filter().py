#Even number from a list 
# list=[23,44,12,21,34]
# def myfunc(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# b=filter(myfunc,list)
# for x in b:
#     print(x)

#word longer than 3 charcacters
# def func(x):
#     return len(x)>3
# words=["Kumar","Aj","Leo","Akash"]
# c=filter(func,words)
# print(list(c))

#remove empty string from a list 
a = ["king", "", "thala", "", "Dhoni"]
b = list(filter(lambda x: x != "", a))
print(b)  


#positive numbers from list 
# def fun(num):
#     return num>0
# int=[7,77,77,888,-7,-78,-56,-43,54]
# e=filter(fun,int)
# print(list(e))


# #name starts with a
# def fun(m):
#     return m.startswith("A")
# word=["Abi","Rakesh","Anu","Anbu","Ravi","Kathir"]
# a=filter(fun,word)
# print(list(a))