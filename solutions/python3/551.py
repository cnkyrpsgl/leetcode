class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return False if "LLL" in s or s.count("A")>1 else True