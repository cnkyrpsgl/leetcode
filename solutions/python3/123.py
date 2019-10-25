class Solution:
    def maxProfit(self, prices):
        s1 = s2 = 0
        b1 = b2 = -float("inf")
        for p in prices:
            if -p > b1: b1 = -p
            if b1 + p > s1: s1 = b1 + p
            if s1 - p > b2: b2 = s1 - p
            if b2 + p > s2: s2 = b2 + p
        return s2