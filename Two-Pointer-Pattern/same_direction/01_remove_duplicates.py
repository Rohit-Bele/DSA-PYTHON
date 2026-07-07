# ==========================================
# Version 1 : My Approach (Using Extra Space)
# ==========================================

def remove_duplicates_extra_space(arr):

    # First element is always unique
    result = [arr[0]]

    left = 0

    for right in range(len(arr)):

        # New unique element found
        if arr[left] != arr[right]:

            left += 1
            arr[left] = arr[right]

            # Store unique element in new array
            result.append(arr[left])

    return result


# ==========================================
# Version 2 : Interview Approach (In-Place)
# ==========================================

def remove_duplicates_inplace(arr):

    # left = last unique element index
    left = 0

    # right explores the array
    for right in range(1, len(arr)):

        # New unique element found
        if arr[left] != arr[right]:

            left += 1

            # Move unique element forward
            arr[left] = arr[right]

    # left stores last unique index
    # unique count = last index + 1
    return left + 1


# ==========================================
# Testing Version 1
# ==========================================

arr1 = [1, 1, 2, 3, 3, 4, 5, 5]

result = remove_duplicates_extra_space(arr1)

print("Extra Space Version:")
print(result)

# Output:
# [1, 2, 3, 4, 5]


# ==========================================
# Testing Version 2
# ==========================================

arr2 = [1, 1, 2, 3, 3, 4, 5, 5]

count = remove_duplicates_inplace(arr2)

print("\nIn-Place Version:")
print("Unique Count :", count)

# Only first 'count' elements are valid
print(arr2[:count])

# Same as above:
# for i in range(count):
#     print(arr2[i], end=" ")

# Output:
# Unique Count : 5
# [1, 2, 3, 4, 5]