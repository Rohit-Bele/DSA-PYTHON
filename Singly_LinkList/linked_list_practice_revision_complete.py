# ============================================================
# LINKED LIST — PRACTICE + REVISION FILE
# ============================================================
#
# This file contains:
# 1. Node creation
# 2. Connecting nodes
# 3. Traversal
# 4. Insert at beginning
# 5. Insert at end
# 6. Insert at specific position
# 7. Delete at beginning
# 8. Delete at end
# 9. Delete at specific position
# 10. Edge cases
# 11. Pointer/reference notes
# 12. Complexity + quick revision
#
# IMPORTANT:
# This file is for learning and revision.
# Try to rewrite each operation from memory instead of
# only reading the code.
# ============================================================


# ============================================================
# 1. NODE CLASS
# ============================================================
#
# Every linked-list node contains two important things:
#
#     data → the value stored inside the node
#     next → reference/address of the next node
#
# Example:
#
#     [10 | address of next node]
#
# If there is no next node:
#
#     [10 | None]
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ============================================================
# 2. CREATE AND CONNECT NODES
# ============================================================
#
# We create individual nodes first.
#
# node1 = [5 | None]
# node2 = [10 | None]
# node3 = [15 | None]
# node4 = [20 | None]
#
# Then we connect them using .next:
#
#     5 → 10 → 15 → 20 → None
#
# head stores the reference to the FIRST node.
# ============================================================

node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

head = node1

node1.next = node2
node2.next = node3
node3.next = node4


# ============================================================
# 3. TRAVERSAL / PRINT ALL NODES
# ============================================================
#
# current starts from head and moves one node at a time.
#
#     current = head
#     current = current.next
#
# Think:
#
#     current = "Where am I currently?"
#
# We continue while current is not None.
#
#     while current:
#
# This means:
#     "Keep going while the current node exists."
#
# Time Complexity: O(n)
# Extra Space: O(1)
# ============================================================

def print_all_node(head):
    print()
    current = head

    while current:
        print(current.data, end=" ")
        current = current.next


print_all_node(head)


# ============================================================
# 4. INSERT AT BEGINNING
# ============================================================
#
# Current:
#
#     head
#      ↓
#     5 → 10 → 15 → 20
#
# Suppose we want to insert 2.
#
# new_node = 2
#
# Step 1:
#
#     new_node.next = head
#
# Now:
#
#     2 → 5 → 10 → 15 → 20
#
# Step 2:
#
#     head = new_node
#
# Now head points to 2:
#
#     head
#      ↓
#     2 → 5 → 10 → 15 → 20
#
# MAIN IDEA:
# New node points to the old first node,
# then head is updated to the new node.
#
# Time Complexity: O(1)
# ============================================================

def insert_at_beginning(new_node, head):
    new_node.next = head
    head = new_node
    return head


node5 = Node(2)
head = insert_at_beginning(node5, head)

print_all_node(head)


# ============================================================
# 5. INSERT AT END
# ============================================================
#
# Current:
#
#     2 → 5 → 10 → 15 → 20
#
# Suppose we want to insert 25.
#
# The head does NOT change.
# We need to reach the last node.
#
# To find the last node:
#
#     while current.next:
#         current = current.next
#
# Why current.next?
#
#     while current:
#         → allows current to become None
#
#     while current.next:
#         → stops while current is still the last node
#
# At the last node:
#
#     current → 20
#     current.next → None
#
# Then:
#
#     current.next = new_node
#
# Result:
#
#     2 → 5 → 10 → 15 → 20 → 25
#
# Time Complexity: O(n)
# Extra Space: O(1)
# ============================================================

def insert_at_end(new_node, head):
    current = head

    while current.next:
        current = current.next

    current.next = new_node


node5 = Node(25)
insert_at_end(node5, head)

print_all_node(head)


# ============================================================
# 6. INSERT AT SPECIFIC POSITION
# ============================================================
#
# We use 1-based positions.
#
# Example:
#
#     2 → 5 → 10 → 15 → 20 → 25
#
# Insert 1 at position 4.
#
# Expected:
#
#     2 → 5 → 10 → 1 → 15 → 20 → 25
#
# At the insertion point we need:
#
#     prev → current
#
# Example:
#
#     10 → 15
#
# Insert 1 between them:
#
#     10 → 1 → 15
#
# Steps:
#
#     new_node.next = current
#     prev.next = new_node
#
# IMPORTANT:
# We first connect new_node to current so we don't lose
# the remaining part of the list.
#
# Edge case:
# position == 1
# There is no previous node.
# In that case, insertion at beginning must be handled
# separately.
#
# Time Complexity: O(n)
# Extra Space: O(1) excluding the new node
# ============================================================

def insert_at_position(new_node, head, position):

    # Position 1 means inserting before the current head.
    if position == 1:
        new_node.next = head
        return new_node

    prev = None
    current = head

    for i in range(1, position):
        if current is None:
            return head

        prev = current
        current = current.next

    prev.next = new_node
    new_node.next = current

    return head


node6 = Node(1)
head = insert_at_position(node6, head, 4)

print_all_node(head)


# ============================================================
# 7. DELETE AT BEGINNING
# ============================================================
#
# Current:
#
#     head
#      ↓
#     2 → 5 → 10 → 15 → 20 → 25
#
# We want to remove 2.
#
# The second node is already accessible through:
#
#     head.next
#
# So:
#
#     head = head.next
#
# Result:
#
#     head
#      ↓
#     5 → 10 → 15 → 20 → 25
#
# We don't need to manually move or delete the old node.
# Once head no longer points to it, it is no longer part
# of the linked list.
#
# Edge cases:
#     head is None → empty list
#     only one node → head becomes None
#
# Time Complexity: O(1)
# ============================================================

def delete_at_beginning(head):

    if head is None:
        return None

    head = head.next
    return head


head = delete_at_beginning(head)

print_all_node(head)


# ============================================================
# 8. DELETE AT END
# ============================================================
#
# Example:
#
#     5 → 10 → 15 → 20 → 25
#
# We want to remove 25.
#
# To remove the last node, we need the SECOND-LAST node.
#
# We use:
#
#     prev → previous node
#     current → current node
#
# Start:
#
#     prev = None
#     current = head
#
# Move both:
#
#     prev = current
#     current = current.next
#
# But we must stop when current is the LAST node.
#
# Therefore:
#
#     while current.next:
#
# At the end:
#
#     prev    → 20
#     current → 25
#
# Then:
#
#     prev.next = None
#
# Result:
#
#     5 → 10 → 15 → 20
#
# IMPORTANT:
#
#     while current
#     → current eventually becomes None
#
#     while current.next
#     → current stops at the last node
#
# Edge cases:
#     empty list
#     one-node list
#
# Time Complexity: O(n)
# Extra Space: O(1)
# ============================================================

def delete_at_end(head):

    # Empty list
    if head is None:
        return None

    # Only one node
    if head.next is None:
        return None

    prev = None
    current = head

    while current.next:
        prev = current
        current = current.next

    prev.next = None

    return head


head = delete_at_end(head)

print_all_node(head)


# ============================================================
# 9. DELETE AT SPECIFIC POSITION
# ============================================================
#
# Example:
#
#     5 → 10 → 15 → 20
#
# Delete position 3.
#
# We need:
#
#     prev     current     next
#       ↓         ↓          ↓
#      10        15         20
#
# We remove current by changing the previous node's link:
#
#     prev.next = current.next
#
# Before:
#
#     10 → 15 → 20
#
# After:
#
#     10 ─────→ 20
#
# Result:
#
#     5 → 10 → 20
#
# The loop's job is ONLY to find the correct prev/current.
#
# Edge cases:
#     head is None
#     position == 1
#     position is outside the list
#     only one node
#
# Time Complexity: O(n)
# Extra Space: O(1)
# ============================================================

def delete_at_position(head, position):

    # Empty list
    if head is None:
        return head

    # Position 1 means deleting the head
    if position == 1:
        return head.next

    prev = None
    current = head

    for i in range(1, position):
        if current is None:
            return head

        prev = current
        current = current.next

    # Position is beyond the list
    if current is None:
        return head

    # Skip the current node
    prev.next = current.next

    return head


head = delete_at_position(head, 3)

print_all_node(head)


# ============================================================
# 10. IMPORTANT POINTER / REFERENCE CONCEPTS
# ============================================================
#
# NODE:
#
#     node.data
#     → value stored inside the node
#
#     node.next
#     → reference/address of the next node
#
#
# HEAD:
#
#     head
#     → reference to the first node
#
# If:
#
#     head → 5 → 10 → 15
#
# Then:
#
#     head.data       → 5
#     head.next       → reference to node 10
#     head.next.data  → 10
#
#
# CURRENT:
#
#     current = head
#
# means current starts at the first node.
#
#     current = current.next
#
# moves current to the next node.
#
# Mental model:
#
#     current = "Where am I currently?"
#
#
# PREV:
#
# prev usually stores the node BEFORE current.
#
#     prev → current → next
#
# This is useful when we need to change a connection.
# ============================================================


# ============================================================
# 11. COMMON TRAVERSAL CONDITIONS
# ============================================================
#
# A) while current:
#
#     while current:
#         current = current.next
#
# Meaning:
#     "Continue while the current node exists."
#
# Eventually:
#
#     current → None
#
#
# B) while current.next:
#
#     while current.next:
#         current = current.next
#
# Meaning:
#     "Continue while there is another node after current."
#
# This stops at the LAST node.
#
#
# Example:
#
#     10 → 20 → 30 → None
#
# When current is 30:
#
#     current       → 30
#     current.next  → None
#
# Loop stops.
#
#
# C) prev + current traversal
#
#     prev = None
#     current = head
#
#     while current:
#         prev = current
#         current = current.next
#
# At the end:
#
#     prev    → last node
#     current → None
#
# This is useful when you need the node that was visited
# immediately before current.
# ============================================================


# ============================================================
# 12. INSERTION vs DELETION — CORE PATTERN
# ============================================================
#
# INSERTION:
#
# Before:
#
#     prev → next
#
# After:
#
#     prev → new_node → next
#
# Main link changes:
#
#     new_node.next = next/current
#     prev.next = new_node
#
#
# DELETION:
#
# Before:
#
#     prev → current → next
#
# After:
#
#     prev ─────────→ next
#
# Main link change:
#
#     prev.next = current.next
#
#
# Think:
#
# INSERT = put a node INTO the chain
# DELETE = skip a node in the chain
# ============================================================


# ============================================================
# 13. EDGE CASE CHECKLIST
# ============================================================
#
# Before finalizing a Linked List function, ask:
#
# 1. What if the list is empty?
#
#     head = None
#
# 2. What if there is only one node?
#
#     head.next = None
#
# 3. What if position == 1?
#
#     There is no previous node.
#
# 4. What if position is greater than the list length?
#
#     current may become None.
#
# 5. What if we are deleting the last node?
#
#     We need the second-last node.
#
# 6. Does the head change?
#
#     Insert/delete at beginning → YES
#     Insert/delete at end → normally NO
#     Middle operation → normally NO
#
# Good habit:
#
#     "What unusual situation can break my normal logic?"
# ============================================================


# ============================================================
# 14. TIME COMPLEXITY QUICK REVISION
# ============================================================
#
# Insert at beginning:
#     O(1)
#
# Delete at beginning:
#     O(1)
#
# Search:
#     O(n)
#
# Traverse:
#     O(n)
#
# Insert at end (without tail pointer):
#     O(n)
#
# Delete at end (without tail pointer):
#     O(n)
#
# Insert at specific position:
#     O(n) in the general case
#
# Delete at specific position:
#     O(n) in the general case
#
# Extra space for pointer variables:
#     O(1)
# ============================================================


# ============================================================
# 15. LINKED LIST QUICK CHEAT SHEET
# ============================================================
#
# CREATE NODE:
#
#     node = Node(value)
#
#
# ACCESS VALUE:
#
#     node.data
#
#
# ACCESS NEXT NODE:
#
#     node.next
#
#
# START TRAVERSAL:
#
#     current = head
#
#
# MOVE FORWARD:
#
#     current = current.next
#
#
# INSERT BEGINNING:
#
#     new_node.next = head
#     head = new_node
#
#
# INSERT END:
#
#     while current.next:
#         current = current.next
#     current.next = new_node
#
#
# INSERT MIDDLE:
#
#     new_node.next = current
#     prev.next = new_node
#
#
# DELETE BEGINNING:
#
#     head = head.next
#
#
# DELETE END:
#
#     while current.next:
#         prev = current
#         current = current.next
#     prev.next = None
#
#
# DELETE MIDDLE:
#
#     prev.next = current.next
#
#
# MAIN IDEA:
#
# Most Linked List problems are about two things:
#
# 1. Which node is my pointer currently pointing to?
# 2. Which .next connection needs to change?
#
# If you can answer those two questions,
# the code usually becomes much easier.
# ============================================================
