class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def traverse(node):
            if not node: return 0
            return max(traverse(node.left), traverse(node.right)) * 2 + 1
        length = traverse(root)
        stack, dic, res, padding = [root], {root : length // 2}, [], length // 2
        while any(stack):
            out, tmp, padding = [""] * length, [], padding // 2
            for i, node in enumerate(stack):
                out[dic[node]] = str(node.val)
                if node.left:
                    dic[node.left] = dic[node] - padding - 1
                    tmp.append(node.left)
                if node.right:
                    dic[node.right] = dic[node] + padding + 1
                    tmp.append(node.right)
            res.append(out)
            stack = tmp
        return res