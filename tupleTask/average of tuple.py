numbers=(2,4,6,78)
count = 0
total=0
for i in numbers:
    total += i
    count += 1
if count == 0:
    print("List is empty.")
else:
    average = total / count
    print("Average no is:", average)
