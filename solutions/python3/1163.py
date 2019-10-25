class Solution:
    def lastSubstring(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            result = max(result, s[i:])
        return result
        