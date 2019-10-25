class Solution:
    def connect(self, root: "Node") -> "Node":
        if root == None:
            return root
        q, prev = [(root, 1)], None
        while q:
            curr, pos = q.pop(0)
            if prev != None and prev[1] == pos:
                prev[0].next = curr
            prev = [curr, pos]
            if curr.left:
                q.append((curr.left, pos + 1))
            if curr.right:
                q.append((curr.right, pos + 1))
        return root

