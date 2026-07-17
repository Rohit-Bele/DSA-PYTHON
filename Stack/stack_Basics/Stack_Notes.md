# Stack (LIFO)

## Definition

A Stack is a linear data structure that follows:

```text
LIFO = Last In First Out
```

The element inserted last is removed first.

Example:

```text
Push 10
Push 20
Push 30

Stack:
30 ← Top
20
10

Pop →

30 removed first
```

---

## Real-Life Examples

### Stack of Plates

```text
Top Plate Removed First
```

### Browser Back Button

```text
Page A
Page B
Page C

Back → C removed
Back → B removed
```

### Undo Feature

```text
Type A
Type B
Type C

Undo → C removed
```

---

## Operations

### Push

Insert an element.

```python
stack.append(10)
```

Time Complexity:

```text
O(1)
```

---

### Pop

Remove top element.

```python
stack.pop()
```

Time Complexity:

```text
O(1)
```

---

### Peek / Top

View top element without removing.

```python
stack[-1]
```

Time Complexity:

```text
O(1)
```

---

### Is Empty

Check whether stack is empty.

```python
len(stack) == 0
```

Time Complexity:

```text
O(1)
```

---

## Stack in Python

### Create Stack

```python
stack = []
```

---

### Push

```python
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
```

Output:

```text
[10, 20, 30]
```

---

### Pop

```python
stack.pop()

print(stack)
```

Output:

```text
[10, 20]
```

---

### Peek

```python
print(stack[-1])
```

Output:

```text
20
```

---

## Visualization

```text
Push 10

10
↑ Top

----------------

Push 20

20
10
↑ Top

----------------

Push 30

30
20
10
↑ Top

----------------

Pop

20
10
↑ Top
```

---

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Is Empty | O(1) |

---

## When to Use Stack

Use Stack when:

```text
Need Last-In-First-Out behavior

Undo Operations

Browser History

Expression Evaluation

Balanced Parentheses

DFS (Depth First Search)

Recursion
```

---

## Common Interview Questions

### Easy

```text
Valid Parentheses

Remove Adjacent Duplicates

Implement Stack using Queue
```

### Medium

```text
Daily Temperatures

Next Greater Element

Evaluate Reverse Polish Notation
```

### Hard

```text
Largest Rectangle in Histogram

Trapping Rain Water
```

---

## Recognition Trick

Ask:

```text
Do I need the most recently added item first?
```

If YES:

```text
Use Stack
```

---

## Python Stack Template

```python
stack = []

# Push
stack.append(x)

# Pop
stack.pop()

# Peek
top = stack[-1]

# Empty
if not stack:
    print("Empty")
```

---

## Summary

```text
Stack = LIFO

Push  -> append()
Pop   -> pop()
Peek  -> stack[-1]

Most Used Questions:
1. Valid Parentheses
2. Next Greater Element
3. Daily Temperatures
4. Monotonic Stack Problems
```