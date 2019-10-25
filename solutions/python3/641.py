class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
        
class MyCircularDeque:

    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1
        
    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1
    
    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize:
            return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size