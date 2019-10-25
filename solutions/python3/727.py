class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T): return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]
            
        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res