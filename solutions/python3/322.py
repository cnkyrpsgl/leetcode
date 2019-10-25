class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1): dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1