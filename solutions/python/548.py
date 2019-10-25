class Solution:
    def splitArray(self, nums):
        n = len(nums)
        s = [0] * (n + 1)
        for i in range(n): s[i + 1] = s[i] + nums[i]
        def check(l, r):
            return set(s[m] - s[l] for m in range(l + 1, r + 1) if s[m] - s[l] == s[r + 1] - s[m + 1])
        return any(check(0, j - 1) & check(j + 1, n - 1) for j in range(n))