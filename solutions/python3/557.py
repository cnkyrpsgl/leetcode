class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        j, s_out=0, str()
        for i, char in enumerate(s):
            if i==len(s)-1: s_out+=s[j:i+1][::-1]; return "".join(s_out)
            if char==" ": s_out+=s[j:i][::-1]; j=i+1; s_out+=" "
        return "".join(s_out)