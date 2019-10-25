class Solution:
    def findDuplicateSubtrees(self, root):
        def dfs(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), dfs(root.left), dfs(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        dfs(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]