# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        q, res, target = deque([root]) if root else None, [root.val] if root else [], root
        while q:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if node == target and q: 
                res.append(max([i.val for i in q]))
                target = q[-1]
        return res