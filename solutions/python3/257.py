# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, arr):
            if not node.right and not node.left:
                #print(arr)
                self.res += ['->'.join(str(num) for num in arr)]
            if node.left:
                dfs(node.left, arr + [node.left.val])
            if node.right:
                dfs(node.right, arr + [node.right.val])
        self.res = []
        if not root: return []
        dfs(root, [root.val])
        return self.res