class Solution:
    def countSubstrings(self, s):       
        res = 0
        for k in range(len(s)):
            i = j = k
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
            i , j =k , k + 1
            while 0 <= i and j < len(s):
                if s[i] == s[j]: res += 1
                else: break
                i , j = i - 1, j + 1
        return res