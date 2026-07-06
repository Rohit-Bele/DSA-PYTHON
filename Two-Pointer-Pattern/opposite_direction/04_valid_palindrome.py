def clear_string(s):
 
    clear_str = ""
    for char in s:
        if char.isalnum():
            clear_str += char.lower()    
    return clear_str



def is_valid_palindrome(s):
    clean = clear_string(s)
    left = 0 
    right = len(clean)-1

    while left < right:
        if clean[left] == clean[right]:
            left+=1
            right-=1
        else:
            return False
    return True

s = "A man, a plan, a canal: Panama"
result = is_valid_palindrome(s)
if result:
    print("it is valid palindrome")
else:
    print("it is not a valid palindrome")
