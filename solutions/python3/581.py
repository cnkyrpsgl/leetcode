class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        i = 0
        for i in range(len(arr)):
            if arr[i] != nums[i]:
                for j in range(len(arr) - 1, -1, -1):
                    if arr[j] != nums[j]:
                        return j - i + 1
        return 0