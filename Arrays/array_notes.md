# 📚 Arrays in Python

## 1. What is an Array?

An array is a collection of elements stored in a contiguous manner.

In Python, we use **Lists** to represent arrays.

### Example

```python
arr = [10, 20, 30, 40, 50]
```

Here:

- `10, 20, 30, 40, 50` are elements
- `arr` is the array name

---

## 2. Characteristics of Arrays

1. Stores multiple values in a single variable
2. Elements are stored using indexes
3. Index starts from `0`
4. Allows random access
5. Can store duplicate values

### Example

```python
arr = [10, 20, 30]
```

| Index | Value |
|---------|---------|
| 0 | 10 |
| 1 | 20 |
| 2 | 30 |

---

## 3. Array Declaration

```python
arr = [10, 20, 30, 40]
```

### Empty Array

```python
arr = []
```

---

## 4. Accessing Elements

```python
arr = [10, 20, 30, 40]

print(arr[0])
```

**Output**

```text
10
```

```python
print(arr[2])
```

**Output**

```text
30
```

---

## 5. Traversing an Array

### Method 1

```python
for num in arr:
    print(num)
```

### Method 2

```python
for i in range(len(arr)):
    print(arr[i])
```

---

## 6. Insertion Operations

### Add at End

```python
arr.append(50)
```

### Example

```python
arr = [10, 20, 30]
arr.append(40)
```

**Output**

```python
[10, 20, 30, 40]
```

### Insert at Specific Position

```python
arr.insert(1, 15)
```

**Output**

```python
[10, 15, 20, 30]
```

---

## 7. Deletion Operations

### Remove by Value

```python
arr.remove(20)
```

### Remove Last Element

```python
arr.pop()
```

### Remove by Index

```python
arr.pop(2)
```

---

## 8. Update Operation

```python
arr = [10, 20, 30]

arr[1] = 100
```

**Output**

```python
[10, 100, 30]
```

---

## 9. Searching

### Linear Search

```python
arr = [10, 20, 30, 40]

target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found")
```

---

## 10. Common Array Problems

1. Find Largest Element
2. Find Smallest Element
3. Find Sum of Elements
4. Linear Search
5. Reverse Array
6. Count Occurrences
7. Find Second Largest Element
8. Remove Duplicates

---

## 11. Time Complexity

| Operation | Complexity |
|------------|------------|
| Access Element | O(1) |
| Search Element | O(n) |
| Insert at End | O(1) |
| Insert at Beginning | O(n) |
| Delete Element | O(n) |
| Traversal | O(n) |

---

## 12. Advantages

- Easy to use
- Fast element access
- Efficient traversal
- Less memory overhead

---

## 13. Disadvantages

- Insertion in middle is costly
- Deletion is costly
- Fixed-size arrays in many languages

---

## 14. Python Array Methods

```python
append()
insert()
remove()
pop()
sort()
reverse()
index()
count()
clear()
```

---

## 15. Summary

### Array = Collection of Elements

### Important Operations

1. Traversal
2. Insertion
3. Deletion
4. Searching
5. Updating

### Most Important Beginner Problems

1. Largest Element
2. Smallest Element
3. Sum of Elements
4. Linear Search
5. Reverse Array

---
