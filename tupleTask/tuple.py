my_tuple = (-12, 15, 0, 20, 0, -7)
positive = []
negative = []
zero = []

for i in my_tuple:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    elif i == 0:
        zero.append(i)

positive_tuple = tuple(positive)
negative_tuple = tuple(negative)
zero_tuple = tuple(zero)

print("Positive numbers:", positive_tuple)
print("Negative numbers:", negative_tuple)
print("Zero numbers:", zero_tuple)
