class Solution:
    def findRelativeRanks(self, nums):
        rank = {n:i>2 and str(i+1) or ["Gold","Silver","Bronze"][i] + ' Medal' for i,n in enumerate(sorted(nums,reverse=True))}
        return [rank[num] for num in nums]