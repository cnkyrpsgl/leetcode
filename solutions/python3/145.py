class Solution:
    def postorderTraversal(self, root):
        ret, stack = [], root and [root]
        while stack:
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in (node.left, node.right) if child]
        return ret[::-1]