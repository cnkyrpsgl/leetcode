class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        visited = {}

        def dfs(node):
            if node and node.val not in visited:
                newNode = Node(node.val, [])
                visited[newNode.val] = newNode
                newNode.neighbors = [
                    visited.get(n.val) or dfs(n) for n in node.neighbors
                ]
                return newNode

        return dfs(node)
