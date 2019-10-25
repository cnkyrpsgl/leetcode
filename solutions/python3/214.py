class Solution:
    def shortestPalindrome(self, s, pre = ""):
        for i in range(1, len(s) // 2 + 2):
            if s[i - 1:].startswith(s[:i][::-1]): pre = s[2* i - 1:][::-1]
            if s[i:].startswith(s[:i][::-1]): pre = s[2* i:][::-1]
        return pre + s