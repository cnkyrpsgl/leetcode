class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0:
            return False
        i = 1
        while i < num:
            i = i * 4
        return i == num
        