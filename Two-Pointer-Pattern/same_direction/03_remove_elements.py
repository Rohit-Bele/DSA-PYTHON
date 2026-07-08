def remove_elements(arr,val):
    left = 0
    for right in arr:
        if right!=val:
            arr[left]=right
            left+=1
    return left

arr=[2,3,3,2,1]
count = remove_elements(arr,2)
for i in range(count):
    print(arr[i])