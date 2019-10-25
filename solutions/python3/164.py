class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        n, mn, mx= len(nums), min(nums), max(nums)
        bSize = max(1, (mx - mn) // n + 1)
        bNum = (mx - mn) // bSize + 1
        buckets = [[float("inf"), -float("inf")] for _ in range(bNum)]
        for num in nums:
            ind = (num - mn) // bSize
            if num < buckets[ind][0]:
                buckets[ind][0] = num
            if num > buckets[ind][1]:
                buckets[ind][1] = num
        gap = 0
        for i in range(1, bNum):
            if buckets[i] == [float("inf"), -float("inf")]:
                buckets[i] = buckets[i - 1]
            gap = max(gap , buckets[i][0] - buckets[i - 1][1])
        return gap