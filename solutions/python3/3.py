class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx, start, chars = 0, 0, {}
        for i in range(len(s)):
            if s[i] in chars and start <= chars[s[i]]: start = chars[s[i]] + 1
            else: mx = max(mx, i - start + 1)
            chars[s[i]] = i
        return mx