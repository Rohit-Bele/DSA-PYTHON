def average_subarray_k(arr,window_size):
    current_window = 0
    for i in range(window_size):
        current_window+=arr[i]
    

    max_avg = current_window / window_size

    for i in range(1,len(arr)-window_size+1):
        left = arr[i-1]
        right = arr[window_size+i-1]
        current_window = current_window -left + right
        avg = current_window / window_size

        if max_avg < avg:
            max_avg = avg

    return max_avg


arr = [2,4,6,1,7,3,5]
ans = average_subarray_k(arr,3)
print(ans)