class Solution:
    def countPalindromicSubsequences(self, S):
        mod, memo = 10 ** 9 + 7, {}
        def dfs(i, j):
            if (i, j) not in memo:
                cnt = 0
                for x in "abcd":
                    try: l, r = S[i:j + 1].index(x) + i, S[i:j + 1].rindex(x) + i
                    except: continue  
                    cnt += l != r and dfs(l + 1, r - 1) + 2 or 1
                memo[(i, j)] = cnt % mod
            return memo[(i, j)]
        return dfs(0, len(S) - 1)