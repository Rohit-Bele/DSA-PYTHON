arr = [12, 45, 77, 23, 64, 66]

# Direct Traversal (Element Access)
for i in arr:
    print(i)

# Traversal Using Index
for i in range(len(arr)):
    print(arr[i])

# Reverse Using Slicing
# [start:end:step]
# step = -1 => reverse
for i in arr[::-1]:
    print(i)

# Reverse Using Index
# start = last index
# stop = -1 (excluded)
# step = -1
for i in range(len(arr)-1, -1, -1):
    print(arr[i])

# Reverse Using Built-in Function
for i in reversed(arr):
    print(i)

# Important:
# arr[i]      -> Access element (O(1))
# for loop    -> Traversal (O(n))
# arr[::-1]   -> Reverse array
# len(arr)    -> Number of elements
# reversed()  -> Built-in reverse iterator