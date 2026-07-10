# Sliding Window Pattern

## Definition

Sliding Window is a technique used to solve problems involving continuous (contiguous) subarrays or substrings efficiently.

Instead of checking every possible subarray, we maintain a window and slide it through the array/string.

---

## Why Use Sliding Window?

Without Sliding Window:

Time Complexity:

O(n²)

Example:

Check every possible subarray.

---

With Sliding Window:

Time Complexity:

O(n)

Reuse previous calculations instead of recalculating everything.

---

## Recognition Clues

Think Sliding Window when you see:

✓ Subarray

✓ Substring

✓ Continuous Elements

✓ Window Size K

✓ Maximum Sum

✓ Minimum Sum

✓ Longest Substring

✓ Shortest Subarray

✓ Average of Subarray

---

## Main Idea

Use two pointers:

```text
left  = start of window

right = end of window
```

Window moves from left to right.

---

## Visualization

Array:

```text
1 2 3 4 5 6
```

Window Size = 3

```text
[1 2 3]
  ↓
[2 3 4]
  ↓
[3 4 5]
  ↓
[4 5 6]
```

---

# Types of Sliding Window

## 1. Fixed Size Window

Window size remains constant.

Example:

Find Maximum Sum Subarray of Size K.

```python
arr = [2,1,5,1,3,2]
k = 3
```

Possible Windows:

```text
[2,1,5]
[1,5,1]
[5,1,3]
[1,3,2]
```

---

### Fixed Window Template

```python
left = 0
window_sum = 0

for right in range(len(arr)):

    window_sum += arr[right]

    if right - left + 1 == k:

        # process answer

        window_sum -= arr[left]
        left += 1
```

---

## 2. Variable Size Window

Window size changes based on a condition.

Example:

Longest Substring Without Repeating Characters.

Process:

```text
Expand Window
↓
Condition Breaks
↓
Shrink Window
↓
Continue
```

---

### Variable Window Template

```python
left = 0

for right in range(len(arr)):

    # expand window

    while condition_not_valid:

        # shrink window

        left += 1

    # update answer
```

---

# Difference Between Two Pointers and Sliding Window

## Two Pointers

Purpose:

```text
Compare Elements
Rearrange Data
Move Pointers
```

Examples:

```text
Pair Sum
Palindrome
Move Zeroes
Remove Element
```

---

## Sliding Window

Purpose:

```text
Process Continuous Subarrays

Find Maximum

Find Minimum

Find Longest

Find Shortest
```

Examples:

```text
Maximum Sum Subarray

Average of Subarray

Longest Substring
```

---

# Complexity

Time Complexity:

```text
O(n)
```

Space Complexity:

```text
O(1)
```

(May vary depending on problem)

---

# Beginner Problems

1. Maximum Sum Subarray of Size K
2. Average of Subarray of Size K
3. Maximum Average Subarray I
4. Maximum Number of Vowels in a Substring
5. Longest Substring Without Repeating Characters

---

# Notes

Fixed Window:

```text
Window size remains constant
```

Variable Window:

```text
Window size changes dynamically
```

---

# Interview Recognition

If the question contains:

```text
Subarray
Substring
Window Size K
Longest
Shortest
Maximum Sum
Minimum Sum
```

Immediately think:

```text
Sliding Window
```

---

# One Line Revision

Sliding Window:

Maintain a continuous window using two pointers and slide it through the array/string to avoid repeated calculations.

---

# Important Formula

Window Size:

```python
right - left + 1
```

Remember:

```text
left  = start of window

right = end of window
```