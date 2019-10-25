class Solution:
    def findMaximumXOR(self, nums, ans = 0):
        ans = 0
        for bit in range(30, -1, -1):
            ans <<= 1
            attempt = ans | 1
            prefix = set()
            for x in nums:
                p = x >> bit
                if attempt ^ p in prefix:
                    ans = attempt
                    break
                prefix.add(p)
        return ans