class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        return 29 + {2: Y % (Y % 25 and 4 or 16) and -1}.get(M, ((M % 2) ^ (M > 7)) + 1)