# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def traverse(node):
            if not node: return 0
            sm = traverse(node.left) + traverse(node.right) + node.val
            if sm in dic: dic[sm] += 1
            else: dic[sm] = 1
            return sm
        dic = {}
        traverse(root)
        mx = max(dic.values())
        return [k for k in dic.keys() if dic[k] == mx]
        
        