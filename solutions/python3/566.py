class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nums_ordered=[x for y in nums for x in y]
        if r*c==len(nums)*len(nums[0]):
            return [nums_ordered[c*i:c*(i+1)] for i in range(r)]
        else:return nums
        