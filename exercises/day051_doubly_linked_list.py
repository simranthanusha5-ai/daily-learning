# Day 51: Doubly Linked List

class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = DNode(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def forward(self):
        curr, res = self.head, []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

dll = DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
print("Forward traversal:", dll.forward())
