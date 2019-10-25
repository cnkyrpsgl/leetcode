class Codec:

    def serialize(self, root):
        q, s = root and collections.deque([root]), ""
        while q:
            node = q.popleft()
            if node is None:
                s += "null#"
            else:
                s += str(node.val) + "#"
                q += [node.left, node.right]
        return s
        

    def deserialize(self, data):
        data = data and collections.deque(data.split("#"))
        q, root = data and collections.deque([TreeNode(int(data.popleft()))]), None
        while q:
            node = q.popleft()
            if not root:
                root = node
            l, r = data.popleft(), data.popleft()
            if l != "null":
                node.left = TreeNode(int(l))
                q.append(node.left)
            if r != "null":
                node.right = TreeNode(int(r))
                q.append(node.right)
        return root