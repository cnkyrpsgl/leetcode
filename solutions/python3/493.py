class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = [0]
        def merge(nums):
            if len(nums) <= 1: return nums
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            for r in right:
                add = len(left) - bisect.bisect(left, 2 * r)
                if not add: break
                res[0] += add
            return sorted(left+right)
        merge(nums)
        return res[0]