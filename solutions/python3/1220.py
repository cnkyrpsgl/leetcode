class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1] * 5
        for _ in range(n - 1):
            add = [0] * 5
            # from a
            add[1] = (add[1] + dp[0]) % mod
            # from e
            add[0] = (add[0] + dp[1]) % mod
            add[2] = (add[2] + dp[1]) % mod
            # from i
            add[0] = (add[0] + dp[2]) % mod
            add[1] = (add[1] + dp[2]) % mod
            add[3] = (add[3] + dp[2]) % mod
            add[4] = (add[4] + dp[2]) % mod
            # from o
            add[2] = (add[2] + dp[3]) % mod
            add[4] = (add[4] + dp[3]) % mod
            # from u
            add[0] = (add[0] + dp[4]) % mod
            for i in range(5):
                dp[i] = add[i] % mod
        return sum(dp) % mod