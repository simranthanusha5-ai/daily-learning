# Day 50: Linked List Reversal

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head: Node | None) -> Node | None:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Construct list 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

reversed_head = reverse_linked_list(head)
output = []
while reversed_head:
    output.append(reversed_head.data)
    reversed_head = reversed_head.next
print("Reversed list:", output)
