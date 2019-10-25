class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        stack, nums, res = [(0, [], 0, k)], range(1, 10), []
        while stack:
            sm, tmp, index, k_val = stack.pop(0)
            for i in range(index, len(nums)):
                if sm + nums[i] < n and k_val > 0: stack.append((sm + nums[i], tmp + [nums[i]], i + 1, k_val - 1))
                elif sm + nums[i] == n and k_val == 1: res.append(tmp + [nums[i]])
        return res