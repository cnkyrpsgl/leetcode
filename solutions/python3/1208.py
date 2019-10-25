class Solution:
    def equalSubstring(self, s: str, t: str, mx: int) -> int:
        i = 0
        for j in range(len(s)):
            mx -= abs(ord(s[j]) - ord(t[j]))
            if mx < 0:
                mx += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1