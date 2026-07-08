def even_numbers(arr):
    left = 0 
    for right in arr:
        if right%2==0:
            arr[left]=right
            left+=1
    return left 

arr=[1,2,3,4,5,6]
count = even_numbers(arr)
for i in range(count):
    print(arr[i])