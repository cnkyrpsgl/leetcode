class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        dp = collections.Counter()
        for a in arr:
            dp[a] = max(dp[a], dp[a - d] + 1)
        return max(dp.values())