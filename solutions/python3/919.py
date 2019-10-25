class CBTInserter:

    def __init__(self, root):
        self.arr, q = [], [root]
        while q:
            self.arr += [node for node in q]
            q = [child for node in q for child in (node.left, node.right) if child]

    def insert(self, v):
        parent = self.arr[(len(self.arr) - 1) // 2]
        if not len(self.arr) % 2:
            child = parent.right = TreeNode(v)
        else:
            child = parent.left = TreeNode(v)
        self.arr += [child]
        return parent.val

    def get_root(self):
        return self.arr[0]