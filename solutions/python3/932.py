class Solution:
    def beautifulArray(self, N):
        if N == 1: return [1]
        half = self.beautifulArray(N - N // 2)
        return [i * 2 - 1 for i in half] + [i * 2 for i in half if i * 2 <= N]