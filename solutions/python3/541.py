class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return "".join([s[i:i+k][::-1]+s[i+k:i+2*k]   if len(s)>=i or len(s)>i-k else s[k*i:][::-1] for i in range(0,len(s),k*2)])