def palindrome(str):
    left = 0
    right = len(str)-1
    
    
    while left < right:
        if str[left] == str[right]:
            left+=1
            right-=1
        else:
            return False
    return True

result = palindrome("maddm")
if result:
    print("it is palindrome")
else:
    print("not a palindrome ")