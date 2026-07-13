def average_of_subarray_k(arr,k):
    avg_sub_arr=[]
    window = 0
    for i in range(k):
        window+=arr[i]

    avg_sub_arr.append(window/k)

    for i in range(1,len(arr)-k+1):
        left = arr[i-1]
        right = arr[k+i-1]

        window = window - left + right
        avg_sub_arr.append(window/k)
    return avg_sub_arr



arr = [1,3,2,6,-1,4,1,8,2]
k = 5

print(average_of_subarray_k(arr,k))
