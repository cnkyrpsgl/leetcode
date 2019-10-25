class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        for i,num in enumerate(nums):
                if num in dic and i-dic[num]<=k:
                    return True
                dic[num]=i
        return False