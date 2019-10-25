class FindElements:
    def dfs(self, node: TreeNode, real: int = 0):
        if node:
            node.val = real
            self.nums.add(node.val)
            self.dfs(node.left, real * 2 + 1)
            self.dfs(node.right, real * 2 + 2)

    def __init__(self, root: TreeNode):
        self.root = root
        self.nums = set()
        self.dfs(root)

    def find(self, target: int) -> bool:
        return target in self.nums
