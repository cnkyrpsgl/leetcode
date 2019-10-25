class Solution:
    def numDecodings(self, s):
        if s[0] == "0": return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            if s[i] == "0" and (s[i - 1] == "0" or s[i - 1] >= "3"): return 0
            dp1, dp2 = [dp2, dp1] if s[i] == "0" else [dp2, dp2 + dp1] if "10" <= s[i -1: i + 1] <= "26" else [dp2, dp2]
        return dp2  