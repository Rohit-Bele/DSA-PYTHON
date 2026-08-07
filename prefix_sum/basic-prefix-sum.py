arr = [2, 4, 1, 6, 3]
for i in range(1,len(arr)):
    arr[i]=arr[i]+arr[i-1]

print("prefix sum:",arr)

arr = [2, 4, 1, 6, 3]

for i in range(len(arr)-2,-1,-1):
    arr[i]+=arr[i+1]

print("suffix sum:",arr)
