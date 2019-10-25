# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = {}
        def traverse(node, parent):
            if not node: return
            dic[node] = [node.val]
            if node.val == sum: res[0] += 1
            if parent:
                for num in dic[parent]:
                    dic[node].append(num + node.val)
                    if num + node.val == sum: res[0] += 1
            traverse(node.left, node)
            traverse(node.right, node)
        res = [0]
        traverse(root, None)
        return res[0]