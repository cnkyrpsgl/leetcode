class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 2: return 0 if not nums else 1 if nums[0] == nums[-1] else 2
        inc = nums[0] < nums[1] if nums[0] != nums[1] else None
        cnt = 2 if inc != None else 1
        for i in range(2, len(nums)):
            if nums[i - 1] != nums[i] and (inc == None or inc != (nums[i - 1] < nums[i])):
                inc = nums[i - 1] < nums[i] 
                cnt += 1
        return cnt