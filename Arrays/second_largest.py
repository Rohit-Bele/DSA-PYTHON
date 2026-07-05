arr = [12, 45, 77, 23, 64, 66]

largest = arr[0]
sec_largest = arr[0]

for num in arr:
    if num > largest:
        sec_largest = largest
        largest = num

    elif sec_largest < num < largest:
        sec_largest = num  

print(sec_largest)