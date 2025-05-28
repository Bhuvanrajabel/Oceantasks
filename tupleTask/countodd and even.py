numbers = (3, 4, 5, 6)
oddlst = []
evenlst = []
for i in numbers:
    if i % 2 != 0:
        oddlst.append(i)
    elif i % 2 == 0:
        evenlst.append(i)
oddtup = tuple(oddlst)
eventup = tuple(evenlst)
print(oddtup)
print(eventup)
