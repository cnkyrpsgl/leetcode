class Solution:
    def canPermutePalindrome(self, s):
        cnt = collections.Counter(s)
        return len([c for c in cnt if cnt[c] % 2]) <= 1