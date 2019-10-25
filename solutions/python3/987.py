class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.arr = []
        def dfs(node, x, y):
            if node:
                self.arr.append((x, y, node.val))
                dfs(node.left, x - 1, y + 1)
                dfs(node.right, x + 1, y + 1)
        dfs(root, 0, 0)
        return [list(map(lambda x: x[-1], g)) for k, g in itertools.groupby(sorted(self.arr), key = lambda x: x[0])]