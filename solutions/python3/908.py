class Solution:
    def smallestRangeI(self, A, K):
        l, r = min(A) + K, max(A) - K 
        return 0 if l >= r else r - l