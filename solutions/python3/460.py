class Node:
    def __init__(self, k, v, f):
        self.key = k
        self.val = v
        self.freq = f
        self.next = self.pre = None
class LFUCache:

    def __init__(self, capacity):
        self.max = capacity
        self.cache = 0
        self.freqLast = {}
        self.Nodes = {}
        self.head = self.tail = Node("#", "#", "#")
        self.head.next = self.tail
        self.tail.pre = self.head

    def changeFreq(self, key):
        node, f = self.Nodes[key], self.Nodes[key].freq
        if self.freqLast[f] == node:
            if node.pre.freq == f:
                self.freqLast[f] = node.pre
            else:
                self.freqLast.pop(f)
        if f + 1 in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f + 1]
            node.next = node.pre.next
        elif f in self.freqLast:
            node.pre.next = node.next
            node.next.pre = node.pre
            node.pre = self.freqLast[f]
            node.next = node.pre.next
        node.pre.next = node.next.pre = node
        self.freqLast[f + 1] = node
        node.freq += 1
        
    def removeFirst(self):
        node, f = self.head.next, self.head.next.freq
        node.pre.next = node.next
        node.next.pre = node.pre
        self.Nodes.pop(node.key)
        if self.freqLast[f] == node:
            self.freqLast.pop(f)
        self.cache -= 1
    
    def get(self, key):
        if key in self.Nodes:
            self.changeFreq(key)
            return self.Nodes[key].val
        return -1
    def put(self, key, value):
        if key in self.Nodes:
            self.changeFreq(key)
            self.Nodes[key].val = value
        elif self.max:
            if self.cache == self.max:
                self.removeFirst()
            self.cache += 1
            new = Node(key, value, 1)
            if 1 in self.freqLast:
                new.pre = self.freqLast[1]
            else:
                new.pre = self.head
            new.next = new.pre.next
            new.pre.next = new.next.pre = new
            self.freqLast[1] = self.Nodes[key] = new