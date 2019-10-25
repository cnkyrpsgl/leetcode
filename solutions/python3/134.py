class Solution:
    def canCompleteCircuit(self, gas, cost, cur = 0, index = 0):
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            if cur < 0: cur, index = 0, i + 1
        return index if index < len(gas) and sum(gas) >= sum(cost) else -1