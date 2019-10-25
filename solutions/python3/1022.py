# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, r: TreeNode, num = 0) -> int:
        if not r: 
            return 0
        num = (num << 1) + r.val
        return (self.sumRootToLeaf(r.left, num) + self.sumRootToLeaf(r.right, num) if r.left or r.right else num) % (10 ** 9 + 7)