class Solution(object):
    def findLHS(self, nums):
        dic, res = collections.defaultdict(int), 0
        for num in nums: dic[num] += 1
        for k in dic:
            if k + 1 in dic: res = max(res, dic[k] + dic[k + 1])
        return res