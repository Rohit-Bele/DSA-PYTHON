arr = [1000,12, 45, 77, 23, 64,99]


smallest =arr[0]
for i in arr:
    if smallest > i:
        smallest = i

print(smallest)