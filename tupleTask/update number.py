lst = (3, 5, 8, 11, 13, 15, 17, 18)
for num in lst:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
