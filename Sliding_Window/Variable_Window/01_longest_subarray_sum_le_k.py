def longest_subarray_sum_len_k(arr,k):
    left = 0 
    total = 0
    max_len = 0 

    for right in range(len(arr)):
        total+=arr[right]

        while total > k :
            total-=arr[left]
            left+=1
        
        current_len = right-left+1
        max_len = max(max_len,current_len)
    return max_len

arr = [1,1,1,1,10]
k = 3
print(longest_subarray_sum_len_k(arr,k))