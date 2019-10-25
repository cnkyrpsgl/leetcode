class Solution:
    def minDeletionSize(self, A):
        res = 0
        cur = [""] * len(A)
        for col in zip(*A):
            cur2 = list(zip(cur, col))
            if cur2 == sorted(cur2):
                cur = cur2
            else:
                res += 1
        return res