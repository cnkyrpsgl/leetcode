class Solution:
    def numberOfWays(self, num_people):
        self.memo = {0: 1}

        def dp(n):
            if n not in self.memo:
                self.memo[n] = sum(
                    [dp(i - 2) * dp(n - i) for i in range(2, n + 1, 2)]
                ) % (10 ** 9 + 7)
            return self.memo[n]

        return dp(num_people)
