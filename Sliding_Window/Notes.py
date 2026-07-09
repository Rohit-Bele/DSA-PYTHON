# Sliding Window Pattern

## Definition

Sliding Window is a technique used to efficiently solve problems involving contiguous subarrays or substrings.

Instead of recalculating values for every subarray, we maintain a window and slide it through the array/string.

---

## Why Use Sliding Window?

Without Sliding Window:

- Check every possible subarray
- Time Complexity = O(n²)

With Sliding Window:

- Reuse previous calculations
- Time Complexity = O(n)

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

---

## Main Idea

Maintain a window using two pointers.

```text
left → window start

right → window end
```

Window moves from left to right.

---

## Fixed Size Window

Window size remains constant.

Example:

Find maximum sum of subarray of size K.

```python
arr = [1,2,3,4,5]
k = 3
```

Possible windows:

```text
[1,2,3]
[2,3,4]
[3,4,5]
```

---

### Diagram

```text
1 2 3 4 5

L   R
```

Window Size = 3

Move:

```text
1 2 3 4 5

  L   R
```

---

### Formula

```python
window_sum -= arr[left]

left += 1

right += 1

window_sum += arr[right]
```

---

## Variable Size Window

Window size changes based on condition.

Example:

Longest substring without repeating characters.

Window expands and shrinks dynamically.

```text
Expand Window
↓
Condition Violated
↓
Shrink Window
↓
Continue
```

---

## Sliding Window Visualization

```text
Array:

1 2 3 4 5 6

Window:

[1 2 3]
  ↓
[2 3 4]
  ↓
[3 4 5]
  ↓
[4 5 6]
```

---

## Difference Between Two Pointers and Sliding Window

### Two Pointers

Purpose:

```text
Compare elements

Move pointers

Rearrange data
```

Examples:

```text
Pair Sum
Palindrome
Move Zeroes
Remove Element
```

---

### Sliding Window

Purpose:

```text
Process contiguous subarrays/substrings

Find max/min values

Find longest/shortest window
```

Examples:

```text
Maximum Sum Subarray

Longest Substring

Minimum Window
```

---

## Fixed Window Template

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

## Variable Window Template

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

## Complexity

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

## Beginner Problems

1. Maximum Sum Subarray of Size K
2. Average of Subarray of Size K
3. Maximum Number of Vowels in a Substring
4. Longest Substring Without Repeating Characters
5. Longest Repeating Character Replacement

---

## Notes

Fixed Window:

```text
Window size remains constant
```

Variable Window:

```text
Window size changes dynamically
```

---

## One-Line Revision

Sliding Window:

Use two pointers to maintain a continuous window and efficiently process subarrays or substrings without recalculating everything.