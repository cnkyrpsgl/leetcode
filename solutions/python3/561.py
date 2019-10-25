class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum=0
        while nums:
            num1=nums.pop()
            num2=nums.pop()
            sum+=num2
        return sum
            