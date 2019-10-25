class Solution:
    def connect(self, root: "Node") -> "Node":
        dummy = Node(-1, None, None, None)
        tmp = dummy
        res = root
        while root:
            while root:
                if root.left:
                    tmp.next = root.left
                    tmp = tmp.next
                if root.right:
                    tmp.next = root.right
                    tmp = tmp.next
                root = root.next
            root = dummy.next
            tmp = dummy
            dummy.next = None

        return res
