class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic, str = {}, "x" + s[:9]
        for i in range(9, len(s)):
            str = str[1:] + s[i]
            dic[str] = 1 if str not in dic else dic[str] + 1
        return [k for k, v in dic.items() if v > 1]