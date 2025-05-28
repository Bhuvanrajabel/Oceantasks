my_tuple = [1, 2, 5, 6, 8, 9, 3, 4, 8, 9, 1, 8]
duplicates = []
for i in range(len(my_tuple)):
    if my_tuple[i] in my_tuple[i + 1 :]:
        if my_tuple[i] not in duplicates:
            duplicates.append(my_tuple[i])
print("Duplicate elements:", duplicates)
