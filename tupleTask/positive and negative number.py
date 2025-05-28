tuple = (5, -45, 23, -89)
positive = 0
negative = 0
for i in tuple:
    if i > 0:
        positive=positive+1
    elif i < 0:
        negative = negative+1
print("positive number:", positive)
print("negative number:", negative)
