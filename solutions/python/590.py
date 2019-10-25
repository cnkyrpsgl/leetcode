class Solution(object):
    def postorder(self, root):
        ret, stack = [], [root]
        while any(stack):
            node = stack.pop()
            ret.append(node.val)
            stack += [child for child in node.children if child]
        return ret[::-1]