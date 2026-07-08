def move_negative_at_front(arr):
    left = 0
    for right in range(len(arr)):
        if arr[right]<0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
    return arr

arr=[1,-2,3,-4,5,-6]
print(move_negative_at_front(arr))