arr = [1000,12, 45, 77, 23, 64,99]


largest = arr[0]
for i in arr:
    if largest < i:
        largest = i

print(largest)