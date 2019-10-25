class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i < n:
            i *=3
        return i == n