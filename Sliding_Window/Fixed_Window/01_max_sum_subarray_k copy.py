def max_sum_subarray_k(arr,window_size):
    current_window=0
    for i in range(0,window_size,1):
        current_window+=arr[i]
    
    max_window=current_window

    for i in range(1,len(arr)-window_size+1):
        left = arr[i-1]
        right = arr[window_size+i-1]
        current_window = (current_window-left)+right

        if current_window > max_window:
            max_window =current_window
    
    return max_window

arr = [2,4,6,1,7,3,5]
ans = max_sum_subarray_k(arr,3)
print(ans)