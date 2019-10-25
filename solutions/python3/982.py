class Solution:
    def countTriplets(self, A: List[int]) -> int:
        cnt = collections.Counter([a & b for a in A for b in A])
        return sum(cnt[k] for a in A for k in cnt if not a & k)