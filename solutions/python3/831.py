class Solution:
    def maskPII(self, S):
        if "@" in S:
            s = S.lower().split("@")
            return s[0][0] + "*" * 5 + s[0][-1] + "@" + s[1]
        else:
            nums, tmp = {"0","1","2","3","4","5","6","7","8","9"}, ""
            for c in S:
                if c in nums: tmp += c
            return "+" + "*" * (len(tmp) - 10) + "-***-***-" + tmp[-4:] if len(tmp) > 10 else "***-***-" + tmp[-4:]