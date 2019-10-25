class Node:
    def __init__(self, pos):
        self.pos = pos
        self.left = None
        self.right = None
        
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        N = len(flowers)
        ans = -1
        nodes = {0:Node(-float('inf'))}
        for x in range(1, N + 2):
            nodes[x] = Node(x)
            nodes[x].left = nodes[x - 1]
            nodes[x - 1].right = nodes[x]
        nodes[N + 1].pos = float('inf')
        for day in range(N, 0, -1):
            x = flowers[day - 1]
            if nodes[x].pos - nodes[x].left.pos - 1 == k or nodes[x].right.pos - nodes[x].pos - 1 == k:
                ans = day
            nodes[x].left.right = nodes[x].right
            nodes[x].right.left = nodes[x].left
        return ans