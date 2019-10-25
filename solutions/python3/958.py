class Solution:
    def isCompleteTree(self, root):
        q, pre = [root, None], 1
        while any(q):
            i = q.index(None)
            if any(q[i:]) or pre > 1:
                return False
            pre = len(q[i:])
            q = [child for node in q[:i] for child in (node.left, node.right)] + [None]
        return True