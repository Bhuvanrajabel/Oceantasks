list=[[23,112,54],[43,77,99],[21,65,87]]
Add_list=[]
Sum=0
for Data in list:
    Sum=0
    for i in Data:
        Sum+=i
    Add_list.append(Sum)
print(Add_list)