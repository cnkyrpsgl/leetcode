class Solution:
    def countBinarySubstrings(self, s):
        s = s.replace("01", "0#1").replace("10", "1#0").split("#")
        return sum(min(len(s[i]), len(s[i - 1])) for i in range(1, len(s)))