class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        out=even=sum(v for k,v in Counter(s).items() if v%2==0)
        odd_big=[v for k,v in Counter(s).items() if v%2!=0 and v>1]
        odd_small=[v for k,v in Counter(s).items() if v==1]
        if len(odd_big)==1: out+=odd_big[0]
        else:
            out+=sum(odd_big)-len(odd_big)+1  
            if len(odd_small)==0 and len(odd_big)==0: out-=1
        return out