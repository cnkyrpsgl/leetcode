memo = {}
class Solution:
    def countArrangement(self, N, arr = None):
        if not arr: arr = tuple(range(1, N + 1))
        if (N, arr) in memo or N == 1: return N == 1 and 1 or memo[(N, arr)]
        memo[(N, arr)] = sum([self.countArrangement(N-1, arr[:j]+arr[j + 1:]) for j in range(len(arr)) if arr[j]%N==0 or N%arr[j]==0])
        return memo[(N, arr)]