class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        j = 0
        while s and all(j < len(s[i]) and j < len(s[i - 1]) and s[i][j] == s[i - 1][j] for i in range(len(s))):
            j += 1
        return s[0][:j] if j else ''