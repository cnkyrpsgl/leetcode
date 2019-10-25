class Solution:
    def permuteUnique(self, nums):
        dic = set()
        for p in itertools.permutations(nums):
            if p not in dic: 
                dic.add(p)
        return list(dic)