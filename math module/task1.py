list=[2,True,False,4,False,True]
count=0
for i in list:
    if i==True or i==False:
        count+=1
print(count)