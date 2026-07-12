def max_vowels_substring(str,k):
    vowels={'a','e','i','o','u'}
    current_count = 0 
    max_count = 0
    for i in range(k):
        if str[i] in vowels:
            current_count+=1
    max_count = current_count


    for i in range(1,len(str)-k+1):
        left = str[i-1]
        right = str[k+i-1]

        if left in vowels:
            current_count -= 1

        if right in vowels:
            current_count += 1

        max_count = max(max_count, current_count)
    return max_count

s = "abciiidef"
k = 3

print(max_vowels_substring(s,k))

