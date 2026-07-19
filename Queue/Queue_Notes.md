# Queue (FIFO)

## What is a Queue?

A Queue is a linear data structure that follows the **FIFO (First In, First Out)** principle.

- The first element inserted is the first element removed.
- Insertion happens at the **Rear**.
- Deletion happens from the **Front**.

---

# Real Life Examples

- People standing in a queue
- Printer Queue
- Ticket Booking System
- Customer Service Queue
- CPU Scheduling
- BFS (Breadth First Search)

---

# FIFO Principle

```
Front                     Rear

10 → 20 → 30 → 40

Remove from Front
Insert at Rear
```

Example

```
Enqueue(10)

10

Enqueue(20)

10 20

Enqueue(30)

10 20 30

Dequeue()

20 30
```

---

# Queue Operations

## 1. Enqueue

Adds an element at the Rear.

Python

```python
queue.append(10)
```

Time Complexity

```
O(1)
```

---

## 2. Dequeue

Removes an element from the Front.

Python

```python
queue.pop(0)
```

Time Complexity

```
O(n)
```

Why?

Because all elements shift one position.

---

## Better Method

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)

queue.popleft()
```

Time Complexity

```
O(1)
```

---

## 3. Front (Peek)

Returns the first element.

```python
queue[0]
```

Time Complexity

```
O(1)
```

---

## 4. Rear

Returns the last element.

```python
queue[-1]
```

Time Complexity

```
O(1)
```

---

## 5. isEmpty

```python
len(queue) == 0
```

Time Complexity

```
O(1)
```

---

## 6. Size

```python
len(queue)
```

Time Complexity

```
O(1)
```

---

# Queue Visualization

Initially

```
Front Rear

[]
```

Enqueue 10

```
Front Rear

[10]
```

Enqueue 20

```
Front      Rear

[10,20]
```

Enqueue 30

```
Front          Rear

[10,20,30]
```

Dequeue

```
Front      Rear

[20,30]
```

---

# Queue using List

```python
queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.pop(0)

print(queue)
```

Output

```
[10,20,30]

[20,30]
```

---

# Queue using deque (Recommended)

```python
from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

queue.popleft()

print(queue)
```

Output

```
deque([10,20,30])

deque([20,30])
```

---

# Queue Time Complexity

| Operation | List | deque |
|------------|------|--------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(n) | O(1) |
| Front | O(1) | O(1) |
| Rear | O(1) | O(1) |
| Size | O(1) | O(1) |

---

# Queue vs Stack

| Stack | Queue |
|---------|---------|
| LIFO | FIFO |
| Insert at Top | Insert at Rear |
| Remove from Top | Remove from Front |
| append() | append() |
| pop() | popleft() |

---

# Types of Queue

## 1. Simple Queue

FIFO

```
10 → 20 → 30
```

---

## 2. Circular Queue

Last position connects to first position.

Used to efficiently utilize memory.

Applications

- CPU Scheduling
- Buffers
- Operating Systems

---

## 3. Priority Queue

Elements are removed based on priority instead of insertion order.

Example

```
Priority

1
2
3

Highest Priority removed first.
```

Python

```python
import heapq

pq = []

heapq.heappush(pq,3)
heapq.heappush(pq,1)
heapq.heappush(pq,2)

print(heapq.heappop(pq))
```

Output

```
1
```

---

## 4. Deque (Double Ended Queue)

Insertion and deletion can happen from both ends.

Python

```python
from collections import deque

dq = deque()

dq.append(10)

dq.appendleft(5)

dq.pop()

dq.popleft()
```

Applications

- Sliding Window
- Palindrome
- Cache

---

# Applications of Queue

- Breadth First Search (BFS)
- CPU Scheduling
- Printer Queue
- Call Center
- Ticket Booking
- Buffer
- Networking
- Messaging Systems
- Task Scheduling

---

# Queue Pattern Recognition

If the question contains words like

- First Come First Serve
- Process in Order
- Level Order Traversal
- Waiting Line
- BFS
- Scheduler
- Buffer

Think

```
QUEUE
```

---

# Common Mistakes

❌ Using pop()

```python
queue.pop()
```

Removes from Rear.

Not Queue.

---

✅ Correct

```python
queue.popleft()
```

---

❌ Using List for heavy Queue operations.

Use

```python
collections.deque
```

---

# Interview Tips

Remember

```
Stack
↓

LIFO

Queue
↓

FIFO
```

---

# Important Python Methods

```python
append()

appendleft()

pop()

popleft()

len()

queue[0]

queue[-1]
```

---

# LeetCode Queue Problems (Future Practice)

Easy

- Implement Queue using Stacks
- Number of Recent Calls
- Moving Average from Data Stream

Medium

- Design Circular Queue
- Dota2 Senate
- Open the Lock

Hard

- Sliding Window Maximum
- Shortest Subarray with Sum at Least K

---

# Summary

✔ FIFO

✔ Insert at Rear

✔ Delete from Front

✔ deque is preferred over list

✔ enqueue -> append()

✔ dequeue -> popleft()

✔ Front -> queue[0]

✔ Rear -> queue[-1]

✔ Time Complexity

enqueue -> O(1)

dequeue -> O(1) using deque