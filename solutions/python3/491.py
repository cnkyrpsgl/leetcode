class Solution:
    def findSubsequences(self, nums):
        subs = {()}
        for num in nums:
            subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
        return [sub for sub in subs if len(sub) >= 2]