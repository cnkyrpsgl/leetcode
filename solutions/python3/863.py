class Solution:
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], collections.defaultdict(int)
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)
        dfs(root)
        def dfs2(node, d):
            if d < K:
                visited[node] = 1
                for v in adj[node]:
                    if not visited[v]:
                        dfs2(v, d + 1)
                visited[node] = 0
            else:
                res.append(node.val)
        dfs2(target, 0)
        return res