# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.k, self.res = 0, None
    def kthSmallest(self, root, k):
        if self.k < k and root.left: self.kthSmallest(root.left, k)
        self.k += 1
        if self.k == k: self.res = root.val
        if self.k < k and root.right: self.kthSmallest(root.right, k)
        return self.res