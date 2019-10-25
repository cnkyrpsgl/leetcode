class Solution:
    def treeToDoublyList(self, root):
        head, tail = [None], [None]
        def dfs(node, pre):
            if not node:
                return
            l = dfs(node.left, pre)
            new = Node(node.val, l or pre, None)
            if pre and not l:
                pre.right = new
            elif l:
                l.right = new
            if not pre and not l:
                head[0] = new
            if not tail[0] or node.val > tail[0].val:
                tail[0] = new
            r = dfs(node.right, new)
            return r if r else new
        dfs(root, None)
        if head[0]:
            head[0].left = tail[0]
            tail[0].right = head[0]
        return head[0]