class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        a = sorted(k for k, v in cnt.items() if v == 1)
        return a[-1] if a else -1
        