class Solution:
    def reorderedPowerOf2(self, N):
        cnt = collections.Counter(str(N))
        return any(cnt == collections.Counter(str(1 << c)) for c in range(32))