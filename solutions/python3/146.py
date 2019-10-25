class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = self.pre = None
        self.pre = None
class LRUCache:
    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.dic.pop(node.key)
        
    def add(self, node):
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = self.tail.pre = node
        self.dic[node.key] = node
        
    def __init__(self, capacity):
        self.dic = {}
        self.n = capacity
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
            
    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.add(node)
        if len(self.dic) > self.n:
            self.remove(self.head.next)