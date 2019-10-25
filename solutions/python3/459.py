class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return True if len(s)>1 and (s in [s[:i]*(len(s)//i) for i in range(2,len(s)) if len(s)%i==0]  or s==s[0]*len(s)) else False 