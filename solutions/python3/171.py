class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(char)-64)*(26**i) for i,char in enumerate(s[::-1])])