class Solution:
    def isSameTree(self, p, q):
        return p == q if not p or not q else p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)