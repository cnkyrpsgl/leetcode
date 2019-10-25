class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        left, right, res = 0, n+1, [None]*n
        for i in range(n):
            if k == 1:
                if i%2 == 0:
                    while i<n: res[i], right, i = right - 1, right - 1, i + 1 
                else:
                    while i<n: res[i], left, i = left + 1, left + 1, i + 1
                return res
            else:
                if i%2 != 0: res[i], right = right - 1, right - 1
                else: res[i], left = left + 1, left + 1
                if i != 0: k -= 1