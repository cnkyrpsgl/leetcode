class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        dif, dup = [[s1, B[i]] for i, s1 in enumerate(A) if s1 != B[i]], len(A) != len(set(A))
        return len(dif) == 2 and dif[0] == dif[1][::-1] or (not dif and dup)