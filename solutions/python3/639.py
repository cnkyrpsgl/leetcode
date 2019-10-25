class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        if s[0] == "*": dp2 = 9
        for i in range(1, len(s)):
            couple, newDp1 = s[i -1: i + 1], dp2
            if s[i] == "0":
                if s[i - 1] == "0" or s[i - 1] >= "3": return 0
                dp2 = 2 * dp1 if s[i - 1] == "*" else dp1
            elif s[i] == "*":
                dp2 *= 9
                if s[i - 1] == "2": dp2 += 6 * dp1
                elif s[i - 1] == "1": dp2 += 9 * dp1
                elif s[i - 1] == "*": dp2 += 15 * dp1
            elif "10" <= couple <= "26": dp2 += dp1
            elif s[i - 1] == "*": dp2 += 2 * dp1 if s[i] <= "6" else dp1
            dp1 = newDp1
        return dp2 % (10 ** 9 + 7)  