class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cons=[0,0]
        for num in nums:
            if num==1:cons[1]+=1
            else:cons[1]=0
            cons[0]=max(cons[0],cons[1])
        return cons[0]
        