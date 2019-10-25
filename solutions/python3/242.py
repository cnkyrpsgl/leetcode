class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #return sum([ord(i) for i in s])==sum([ord(j) for j in t]) and set(s)==set(t)
        return sorted(s)==sorted(t)