class Solution:
    def isOneEditDistance(self, s, t):
        l1, l2, cnt, i, j = len(s), len(t), 0, 0, 0
        while i < l1 and j < l2:
            if s[i] != t[j]:
                cnt += 1
                if l1 < l2:
                    i -= 1
                elif l1 > l2:
                    j -= 1
            i += 1
            j += 1
        l = abs(l1 - l2)
        return (cnt == 1 and l <= 1)  or (cnt == 0 and l == 1)