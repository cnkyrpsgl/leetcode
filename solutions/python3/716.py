class Node:
    def __init__(self, value, index):
        self.val = value
        self.i = index
        self.pre = self.next = None
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.Nodes = {}
        self.head = self.tail = Node(0, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        newNode = Node(x, self.tail.pre.i + 1)
        newNode.pre = self.tail.pre
        newNode.next = self.tail
        self.tail.pre.next = self.tail.pre = newNode
        self.Nodes[newNode.i] = newNode
        heapq.heappush(self.heap, (-x, -newNode.i))

    def pop(self):
        """
        :rtype: int
        """
        node = self.tail.pre
        node.pre.next = self.tail
        self.tail.pre = node.pre
        self.Nodes.pop(node.i)
        if node.i == -self.heap[0][1]:
            heapq.heappop(self.heap)
        return node.val

    def top(self):
        """
        :rtype: int
        """
        return self.tail.pre.val

    def peekMax(self):
        """
        :rtype: int
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self):
        """
        :rtype: int
        """
        while -self.heap[0][1] not in self.Nodes or self.Nodes[-self.heap[0][1]].val != -self.heap[0][0]:
            heapq.heappop(self.heap)
        node = self.Nodes.pop(-self.heap[0][1])
        node.pre.next = node.next
        node.next.pre = node.pre
        return -heapq.heappop(self.heap)[0]


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()