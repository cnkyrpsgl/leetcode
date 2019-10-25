class Solution:
    def new21Game(self, N, K, W):
        if K == 0 or N >= K + W: return 1
        dp = [1.0] + [0.0] * N
        Wsum, res = 1.0, 0.0
        for i in range(1, N + 1):
            dp[i] += Wsum / W
            if i < K: Wsum += dp[i]
            else: res += dp[i]
            if i - W >= 0: Wsum -= dp[i - W]
        return res