class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        root, mn, mx = head, Node(float("inf"), None), Node(-float("inf"), None)
        while True:
            if head.val > mx.val:
                mx = head
            if head.val < mn.val:
                mn = head
            if head.val <= insertVal <= head.next.val or insertVal >= head.val > head.next.val:
                node = Node(insertVal, head.next)
                head.next = node
                return root
            head = head.next
            if head == root:
                break
        if insertVal > mx.val:
            node = Node(insertVal, mx.next)
            mx.next = node
        else:
            node = Node(insertVal, mn.next)
            mn.next = node
            mn.val, node.val = node.val, mn.val
        return root