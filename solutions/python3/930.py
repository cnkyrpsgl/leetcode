class Solution:
    def numSubarraysWithSum(self, A, S):
        res, sm, sums = 0, 0, collections.defaultdict(int)
        for a in A:
            sm += a
            res += sums[sm - S] + (sm == S)
            sums[sm] += 1
        return res