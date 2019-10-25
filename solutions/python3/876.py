class Solution:
    def middleNode(self, head):
        root, n = head, 0
        while head:
            head = head.next
            n += 1
        for _ in range(n // 2):
            root = root.next
        return root  