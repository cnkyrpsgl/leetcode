class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic, stack, res = {root: 1}, [root], 0
        while any(stack):
            tmp, mn ,mx = [], float("inf"), - float("inf")
            for node in stack:
                res = max(res, dic[stack[-1]] - dic[stack[0]] + 1) 
                if node.left: tmp, dic[node.left] = tmp + [node.left], dic[node] * 2 - 1 
                if node.right: tmp, dic[node.right] = tmp + [node.right], dic[node] * 2
            stack = tmp
        return res