# Two Pointers Technique

## Definition

The Two Pointer Technique is a problem-solving approach where two indexes (pointers) are used to traverse an array or string efficiently.

Instead of using nested loops (O(n²)), we try to solve the problem in O(n).

---

## Why Use Two Pointers?

- Reduces unnecessary comparisons
- Optimizes brute-force solutions
- Improves time complexity
- Commonly asked in interviews

---

## When to Use?

Think about Two Pointers when you see:

- Sorted Array
- Pair Sum Problems
- Palindrome Problems
- Reverse String/Array
- Remove Duplicates
- Two Ends of Array/String

---

## Types of Two Pointers

### 1. Opposite Direction

Pointers start from opposite ends.

Example:

```text
[1, 2, 3, 4, 5]

L           R
```

Move:

```text
L →
← R
```

Used In:

- Palindrome Check
- Pair Sum (Sorted Array)
- Reverse String

---

### 2. Same Direction

Both pointers move left to right.

Example:

```text
[1, 1, 2, 2, 3, 4]

L
R
```

Move:

```text
L →
R →
```

Used In:

- Remove Duplicates
- Sliding Window Foundation

---

## Template (Opposite Direction)

```python
left = 0
right = len(arr) - 1

while left < right:

    # logic

    left += 1
    right -= 1
```

---

## Template (Same Direction)

```python
left = 0

for right in range(len(arr)):

    # logic
```

---

## Time Complexity

Most Two Pointer Problems:

```text
Time Complexity  : O(n)
Space Complexity : O(1)
```

---

## Recognition Clues

Ask yourself:

- Can I start from both ends?
- Is the array sorted?
- Do I need a pair?
- Is it a palindrome problem?
- Can I avoid nested loops?

If YES → Think Two Pointers.

---

## Common Interview Questions

1. Palindrome Check
2. Pair Sum
3. Reverse String
4. Remove Duplicates
5. Container With Most Water
6. Trapping Rain Water

---

## Problems Solved

- [ ] Palindrome Check
- [ ] Pair Sum
- [ ] Remove Duplicates
- [ ] Reverse String

---

## Mistakes I Made

- 
- 
- 

---

## Quick Revision

Definition:

Use two indexes to solve problems efficiently and reduce time complexity.

Recognition:

- Sorted Array
- Pair Sum
- Palindrome
- Reverse Problems
- Remove Duplicates

Complexity:

```text
O(n)
```