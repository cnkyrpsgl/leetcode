class Solution:
    def encode(self, s: str) -> str:
        def dfs(i, j):
            if i == j: return s[i]
            if (i, j) not in memo:
                c1 = min((dfs(i, k) + dfs(k + 1, j) if s[i:k + 1] != s[k + 1:j + 1] else '2[' + dfs(i, k) + ']' for k in range(i, j)), key = len)
                c2 = s[i:j + 1]
                memo[(i, j)] = min(c1, c2, key = len)
                for k in range(i, i + (j - i) // 2 + 1):
                    tar, ind, cnt = s[i:k + 1], i, 0
                    while ind + k - i <= j and s[ind:ind + k - i + 1] == tar:
                        cnt += 1
                        ind += k - i + 1
                    c3 = str(cnt) + '[' + tar + ']' + dfs(ind, j) if ind <= j else str(cnt) + '[' + tar + ']'
                    memo[(i, j)] = min(memo[(i, j)], c3, key = len)
            return memo[(i, j)]
        memo = {}
        return dfs(0, len(s) - 1)