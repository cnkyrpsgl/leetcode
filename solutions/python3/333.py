class Solution:
    def largestBSTSubtree(self, root):
        def dfs(node):
            if not node:
                return True, 0, None, None, 0
            lBool, lSize, lMx, lMn, lTree = dfs(node.left)
            rBool, rSize, rMx, rMn, rTree = dfs(node.right)
            lVal = lMx if lMx != None else -float("inf")
            rVal = rMn if rMn != None else float("inf")
            curMx = max(val for val in (lMx, rMx, node.val) if val != None)
            curMn = min(val for val in (lMn, rMn, node.val) if val != None)
            curBool = lBool and rBool and lVal < node.val < rVal 
            return curBool, lSize + rSize + 1, curMx, curMn, curBool and lSize + rSize + 1 or max(lTree, rTree)
        return dfs(root)[4]