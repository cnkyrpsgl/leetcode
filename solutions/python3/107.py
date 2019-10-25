# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """ 
        from collections import deque
        if root is None:
            return []
        levels=list()
        q=deque([root])
        levels.append([i.val for i in q])
        target=root
        while q:
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if node==target:
                if q:
                    levels.append([i.val for i in q])
                    target=q[-1]
        return list(reversed(levels))