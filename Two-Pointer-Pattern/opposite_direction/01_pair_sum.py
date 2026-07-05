def two_pointers(arr,target):
    left = 0
    right = len(arr)-1 

    while left < right:
        total = arr[left]+arr[right]
        if total == target:
            return [arr[left],arr[right]]
        
        elif total > target:
            right-=1
        
        else:
            left+=1
    return[]    



arr = [1,3,5,6,8,11]
target = 4

result = two_pointers(arr,target)
print(result)

