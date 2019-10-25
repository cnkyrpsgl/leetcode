class Solution:
    def maximumSwap(self, num):
        res, num = num, list(str(num))
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    tmp = int("".join(num[:i] + [num[j]] + num[i + 1:j] + [num[i]] + num[j + 1:]))
                    if tmp > res: res = tmp
        return res