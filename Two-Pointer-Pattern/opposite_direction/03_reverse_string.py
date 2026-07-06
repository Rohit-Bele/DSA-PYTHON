def reverse_string(str):
    left = 0 
    right = len(str)-1 

    str_list = list(str)
    while left < right:
        str_list[left],str_list[right] = str_list[right],str_list[left]
        left+=1
        right-=1
    return "".join(str_list)

print(reverse_string("Rohit"))