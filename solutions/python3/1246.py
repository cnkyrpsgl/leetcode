class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(1, n + 1):
            i, j = 0, l - 1
            while j < n:
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + dp[i + 1][j]
                    if arr[i] == arr[i + 1]:
                        dp[i][j] = min(1 + dp[i + 2][j], dp[i][j])
                    for k in range(i + 2, j + 1):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i + 1][k - 1] + dp[k + 1][j], dp[i][j])
                i, j = i + 1, j + 1
        return dp[0][n - 1]
