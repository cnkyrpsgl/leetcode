class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        dic = collections.defaultdict(lambda: Node(0, None, None))
        dic[None] = None
        n = head
        while n:
            dic[n].val = n.val
            dic[n].next = dic[n.next]
            dic[n].random = dic[n.random]
            n = n.next
        return dic[head]
