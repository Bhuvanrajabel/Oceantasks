negtuple = [-1, -2, -3, 5, 6, 7, 8, -90, -98]
for i in negtuple[:]:
    if i < 0:
        negtuple.remove(i)
print(negtuple)
