# class for creating node 

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None


node1 = Node(5)
print(node1.data)

node2 = Node(10)
node3 = Node(15)
node4 = Node(20)


head = node1
node1.next = node2
node2.next = node3
node3.next = node4


def print_all_node(head):
    print()
    current = head 
    while current:
        print(current.data, end=" ")
        current = current.next

print_all_node(head)



def insert_at_beginning(new_node,head):
    new_node.next = head
    head = new_node
    return head

node5 = Node(2)
head = insert_at_beginning(node5,head)
print_all_node(head)



node5 = Node(25)

def insert_at_end(new_node,head):
    prev = 0 
    current = head
    while current:
        prev = current
        current = current.next
    prev.next = new_node

insert_at_end(node5,head)
print_all_node(head)
