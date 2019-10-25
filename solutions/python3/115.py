class Solution:
    def numDistinct(self, s, t):
        chars, index, dp = set(t), collections.defaultdict(list), [0] * len(t)
        for i, c in enumerate(t): index[c] = [i] + index[c]
        for c in s:
            if c in chars:
                for i in index[c]: dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]