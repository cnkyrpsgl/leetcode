class Solution:
    def integerBreak(self, n):
        pre = [0, 1, 1, 2, 4, 6, 9]
        if n < 7:
            return pre[n]
        for i in range(7, n + 1):
            pre.append(max(pre[i - 2] * 2, pre[i - 3] * 3))
        return pre[-1]