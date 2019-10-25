class Solution:
    def reverse(self, x):
        x = int(str(x)[::-1]) if x >= 0 else int("-" + str(x)[::-1][:-1]); return -2 ** 31 <= x <= 2 ** 31 - 1 and x or 0