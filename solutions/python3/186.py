class Solution:
    def reverseWords(self, s):
        l, r, n = 0, len(s) - 1, len(s)
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        l = r = 0
        while r < n:
            while r + 1 < n and s[r + 1] != " ":
                r += 1
            i = r + 2
            while l <= r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l = r = i