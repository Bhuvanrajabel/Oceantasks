numbers = [12, 45, 67, 89, 34, 67, 89]
largest = second_largest = float("-inf")
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float("-inf"):
    print("No second largest number found.")
else:
    print("Second largest number is:", second_largest)
