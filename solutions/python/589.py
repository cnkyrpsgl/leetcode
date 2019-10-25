class Solution(object):
    def preorder(self, root):
        ret, q = [], collections.deque([root])
        while any(q):
            node = q.popleft()
            ret.append(node.val)
            for child in node.children[::-1]:
                if child: q.appendleft(child)
        return ret