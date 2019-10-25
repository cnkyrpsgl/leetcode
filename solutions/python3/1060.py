class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        cur = nums[0]
        for num in nums[1:]:
            if num - cur - 1 >= k:
                break
            else:
                k -= num - cur - 1
            cur = num
        return cur + k