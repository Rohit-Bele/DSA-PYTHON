def linear_search(arr,target):
    for num in arr:
        if num == target:
            return True
    return False



arr = [10, 20, 30, 40, 50]
target = 30

result = linear_search(arr,target)
if(result):
    print("target found")
else:
    print("target not found")