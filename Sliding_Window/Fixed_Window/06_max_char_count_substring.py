def max_char_count_substring(str,k,ch):
    current_count = 0 
    for i in range(k):
        if str[i] == ch :
            current_count+=1

    max_count = current_count

    for i in range(1,len(str)-k+1):
        left = str[i-1]
        right=str[k+i-1]

        if left == ch:
            current_count-=1

        if right == ch:
            current_count+=1

        max_count = max(max_count,current_count)
    return max_count

s = "ababababab"
k = 3
ch = 'a'

print(max_char_count_substring(s,k,ch))