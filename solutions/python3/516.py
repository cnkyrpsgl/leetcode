class Solution:
    def longestPalindromeSubseq(self, s):
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = dp[i + 1][j - 1] + 2 if s[i] == s[j] else max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]