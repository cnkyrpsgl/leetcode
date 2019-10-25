class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
class MyLinkedList:

    def __init__(self):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
        
    def add(self, preNode, val):
        node = Node(val)
        node.pre = preNode
        node.next = preNode.next
        node.pre.next = node.next.pre = node
        self.size += 1
        
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.size -= 1
        
    def forward(self, start, end, cur):
        while start != end:
            start += 1
            cur = cur.next
        return cur
    
    def backward(self, start, end, cur):
        while start != end:
            start -= 1
            cur = cur.pre
        return cur
    
    def get(self, index):
        if 0 <= index <= self.size // 2:
            return self.forward(0, index, self.head.next).val
        elif self.size // 2 < index < self.size:
            return self.backward(self.size - 1, index, self.tail.pre).val
        return -1

    def addAtHead(self, val):
        self.add(self.head, val)

    def addAtTail(self, val):
        self.add(self.tail.pre, val)

    def addAtIndex(self, index, val):
        if 0 <= index <= self.size // 2:
            self.add(self.forward(0, index, self.head.next).pre, val)
        elif self.size // 2 < index <= self.size:
            self.add(self.backward(self.size, index, self.tail).pre, val)

    def deleteAtIndex(self, index):
        if 0 <= index <= self.size // 2:
            self.remove(self.forward(0, index, self.head.next))
        elif self.size // 2 < index < self.size:
            self.remove(self.backward(self.size - 1, index, self.tail.pre))