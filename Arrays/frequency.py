def frequency(arr,target):
    total=0
    for num in arr:
        if num==target:
            total+=1
    return total 


arr = [1, 2, 2, 3, 2, 4]
target = 2

print(frequency(arr,target))