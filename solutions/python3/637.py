# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        q, target, avg = deque([root]), root, [float(root.val)]
        while q:
            node=q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if q and node==target:
                target, sm = q[-1], 0
                for item in q: sm+=item.val
                avg.append(sm/len(q))
        return avg