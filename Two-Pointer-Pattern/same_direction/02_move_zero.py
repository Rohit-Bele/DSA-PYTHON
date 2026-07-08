# ==========================================
# MOVE ZEROES
# Pattern: Two Pointers (Same Direction)
# ==========================================


# ------------------------------------------
# APPROACH 1: Copy Non-Zero + Fill Zeroes
# ------------------------------------------

def move_zeroes_v1(arr):
    left = 0

    # right explores the array
    for right in arr:

        # keep only non-zero values
        if right != 0:
            arr[left] = right
            left += 1

    # fill remaining positions with 0
    while left < len(arr):
        arr[left] = 0
        left += 1

    return arr


arr1 = [0, 1, 0, 3, 4, 5]
print("Approach 1:", move_zeroes_v1(arr1))


# ------------------------------------------
# APPROACH 2: Swap Method
# ------------------------------------------

def move_zeroes_v2(arr):
    left = 0

    # right explores the array
    for right in range(len(arr)):

        # non-zero found
        if arr[right] != 0:

            # place non-zero at correct position
            arr[left], arr[right] = arr[right], arr[left]

            # move destination pointer
            left += 1

    return arr


arr2 = [0, 1, 0, 3, 4, 5]
print("Approach 2:", move_zeroes_v2(arr2))