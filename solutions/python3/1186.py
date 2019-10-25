class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        def cumSum(it):
            sm = mn = 0
            sums = [0] * len(arr)
            for i, num in it:
                sm += num
                sums[i] = sm - mn
                mn = min(mn, sm)
            return sums
        
        lSum = cumSum(enumerate(arr))
        rSum = cumSum(reversed(list(enumerate(arr))))
        res = -float('inf')
        for i, num in enumerate(arr):
            if num >= 0:
                cur = lSum[i] + rSum[i] - num
            else:
                cur = lSum[i] + rSum[i] - 2 * num
            res = max(res, cur)
        return res if any(c >= 0 for c in arr) else max(arr)