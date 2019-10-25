# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(l, r):
            if r < l: return [None]
            arr = []
            for m in range(l, r + 1):
                left = dfs(l, m - 1)
                right = dfs(m + 1, r)
                for lNode in left:
                    for rNode in right:
                        new = TreeNode(m)
                        new.left = lNode
                        new.right = rNode
                        arr.append(new)
            return arr
        res = dfs(1, n)
        return [] if res == [None] else res