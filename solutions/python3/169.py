class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list=dict()
        for num in nums:
            if not num in num_list:
                num_list[num]=1
            else:
                num_list[num]+=1
        return max(num_list, key=num_list.get)