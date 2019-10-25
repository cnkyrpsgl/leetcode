class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ind, res, sm = {0:-1}, 0, 0
        for i, num in enumerate(nums):
            sm += num and 1 or -1
            if sm in ind:
                res = max(res, i - ind[sm])
            else:
                ind[sm] = i
        return res