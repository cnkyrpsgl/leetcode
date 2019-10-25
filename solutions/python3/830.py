class Solution:
    def largeGroupPositions(self, S):
        res = []
        l = r = 0
        for i in range(1, len(S)):
            if S[i] == S[i - 1]: r += 1
            if r - l >= 2 and (S[i] != S[i - 1] or i == len(S) - 1): res.append([l, r])
            if S[i] != S[i - 1]: l = r = i
        return res