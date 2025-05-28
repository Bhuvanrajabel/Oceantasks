rem_zero = [10, 0, 20, 0, 40 ]
for i in rem_zero[:]:
    if i == 0:
        rem_zero.remove(i)
    elif i != 0:
        pass
print(rem_zero)
