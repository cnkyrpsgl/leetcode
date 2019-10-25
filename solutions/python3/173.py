class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.pushAll(cur.right)
        return cur.val

    def hasNext(self) -> bool:
        return self.stack

    def pushAll(self, node):
        while node != None:
            self.stack += (node,)
            node = node.left
