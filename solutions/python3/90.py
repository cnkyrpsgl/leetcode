class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import combinations as cb
        res, dic = [], set()
        for i in range(len(nums) + 1):
            for item in cb(nums, i):
                item = tuple(sorted(item))
                if item not in dic:
                    dic.add(item)
                    res.append(item)
        return res