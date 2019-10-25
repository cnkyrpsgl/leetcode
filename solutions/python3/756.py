class Solution:
    def pyramidTransition(self, bottom, allowed):
        chars, allowed = 'ABCDEFG', set(allowed)
        def dfs(r, q, i):
            if len(r) == 1: 
                return True
            for c in chars:
                if r[i:i+2]+c in allowed and (i==len(r)-2 and dfs(q+c,"",0) or dfs(r,q+c,i+1)): return True
            return False
        return dfs(bottom, "", 0) 