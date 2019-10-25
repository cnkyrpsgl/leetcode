class Solution:
    def convertToBase7(self, num):
        lead = "" if num > 0 else "0" if num == 0 else "-"
        res, num = [], abs(num)
        while num:
            res.append(int(num % 7))
            num //= 7
        return lead + "".join(str(c) for c in res[::-1])