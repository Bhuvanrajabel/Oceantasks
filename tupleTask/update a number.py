numbers = (4, -5, 2, -8, 0, -7)
updated = []
for num in numbers:
    if num < 0:
        updated.append(0)
    else:
        updated.append(num)
a = tuple(updated)
print(a)
