class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def compute_lcs(s, t):
            m, n = len(s), len(t)
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s[i - 1] != t[j - 1]:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + s[i - 1]
            return dp[-1][-1]
        cs = compute_lcs(str1, str2)
        ans = []
        i, j = 0, 0
        m, n = len(str1), len(str2)
        for ch in cs:
            while i < m and str1[i] != ch:
                ans.append(str1[i])
                i += 1
            while j < n and str2[j] != ch:
                ans.append(str2[j])
                j += 1
            ans.append(ch)
            i += 1
            j += 1
        return ''.join(ans) + str1[i:] + str2[j:]