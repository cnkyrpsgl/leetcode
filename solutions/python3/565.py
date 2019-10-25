class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(nums)):
            if i in dic:
                continue
            j=i
            dic[j]=1
            while nums[i]!=j:
                dic[j]+=1
                i=nums[i]
                dic[i]=1
        return max(dic.values())