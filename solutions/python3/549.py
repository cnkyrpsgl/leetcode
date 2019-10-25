class Solution:
    def longestConsecutive(self, root):
        dec, inc = {}, {}
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            incL = inc[node.left] + 1 if node.left and node.val == node.left.val + 1 else 1
            incR = inc[node.right] + 1 if node.right and node.val == node.right.val + 1 else 1
            inc[node] = max(incL, incR)
            decL = dec[node.left] + 1 if node.left and node.val == node.left.val - 1 else 1
            decR = dec[node.right] + 1 if node.right and node.val == node.right.val - 1 else 1
            dec[node] = max(decL, decR)
            if node.left and node.right and node.left.val == node.val - 1 and node.right.val == node.val + 1:
                m = inc[node.left] + dec[node.right] + 1
            elif node.left and node.right and node.left.val == node.val + 1 and node.right.val == node.val - 1:
                m = dec[node.left] + inc[node.right] + 1
            else:
                m = 0
            return max(m, l, r, inc[node], dec[node])
        return dfs(root)