class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        pre, mx = 0, -float('inf')
        for j, a in enumerate(A):
            mx = max(mx, pre + a - j)
            pre = max(pre, a + j)
        return mx