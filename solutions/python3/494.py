class Solution:
    def findTargetSumWays(self, nums, S):
        d = {S:1}
        for i in range(len(nums)):
            new_d = collections.defaultdict(int)
            for k, v in d.items():
                new_d[k+nums[i]] += v
                new_d[k-nums[i]] += v
            d = new_d
        return d[0]