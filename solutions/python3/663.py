# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkEqualTree(self, root):
        nodeSum = collections.defaultdict(int)
        def dfs(node):
            if not node: 
                return 0
            sm = node.val + dfs(node.left) + dfs(node.right)
            nodeSum[sm] += 1
            return sm
        totalSum = dfs(root)
        if not totalSum:
            return nodeSum[0] > 1
        return totalSum % 2 == 0 and totalSum // 2 in nodeSum