class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return [k for k in cnt if cnt[k] == 2] + [i for i in range(1, len(nums) + 1) if i not in cnt]