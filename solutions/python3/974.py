class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = sm = 0
        sums = collections.defaultdict(int)
        sums[0] = 1
        for a in A:
            sm = (sm + a) % K
            sums[sm] += 1
            res += sums[sm] - 1
        return res