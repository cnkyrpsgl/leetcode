# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def dfs(parent, s, lev):
            print(parent.val, s, lev)
            if not s: return
            i = lev
            l = 0
            while i < len(s) and s[i].isdigit():
                l = l * 10 + int(s[i])
                i += 1
            parent.left = TreeNode(l)  
            j = lev
            f = '-' * lev
            for ind in range(i, len(s)):
                if s[ind:].startswith(f) and not s[ind:].startswith(f + '-') and s[ind -1] != '-':
                    rr = ind
                    j = ind + lev
                    r = 0
                    while j < len(s) and s[j].isdigit():
                        r = r * 10 + int(s[j])
                        j += 1
                    parent.right = TreeNode(r)
                    dfs(parent.left, s[i:rr], lev + 1)
                    dfs(parent.right, s[j:], lev + 1)
                    return
            dfs(parent.left, s[i:], lev + 1)
        i = num = 0
        while i < len(S) and S[i].isdigit():
            num = num * 10 + int(S[i])
            i += 1
        root = TreeNode(num)
        dfs(root, S[i:], 1)
        return root
            