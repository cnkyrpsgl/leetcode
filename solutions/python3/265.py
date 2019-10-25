class Solution:
    def minCostII(self, costs):
        for i in range(1, len(costs)):
            for j in range(len(costs[0])): costs[i][j] += min(costs[i - 1][:j] + costs[i - 1][j + 1:])
        return costs and min(costs[-1]) or 0