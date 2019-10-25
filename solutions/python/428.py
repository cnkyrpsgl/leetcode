class Codec:

    def serialize(self, root):
        arr = []
        def dfs(node):
            if not node: return
            arr.append(str(node.val))
            for child in node.children:
                dfs(child)
            arr.append("#")
        dfs(root)
        return " ".join(arr)

    def deserialize(self, data):
        if not data: return None
        data = collections.deque(data.split(" "))
        root = Node(int(data.popleft()), [])
        q = [root]
        while data:
            val = data.popleft()
            if val == "#":
                q.pop()
            else:
                new = Node(int(val), [])
                q[-1].children.append(new)
                q.append(new)
        return root