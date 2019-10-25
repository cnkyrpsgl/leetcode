class Solution: 
    def combinationSum2(self, candidates, target):   
        res = []
        self.dfs(sorted(candidates), target, 0, [], res)
        return res
    def dfs(self, nums, target, index, path, res):    
        if target < 0:
            return 
        if target == 0 and path not in res:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            if i>1 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[:i] + nums[i+1:], target-nums[i], i, path+[nums[i]], res)