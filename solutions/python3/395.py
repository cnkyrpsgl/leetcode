class Solution:
    def longestSubstring(self, s, k):
        br = [-1] + [i for i, c in enumerate(s) if s.count(c) < k] + [len(s)]
        return len(s) if len(br) == 2 else max(self.longestSubstring(s[br[i - 1] + 1:br[i]], k) for i in range(1, len(br)))