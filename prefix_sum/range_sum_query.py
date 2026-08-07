def range_sum(arr, left, right):
    if left==0:
        return arr[right]
    if left>right:
        return "0"
    return arr[right]-arr[left-1]


arr = [2, 4, 1, 6, 3]

for i in range(1,len(arr)):
    arr[i]+=arr[i-1]

print(range_sum(arr,1,3))