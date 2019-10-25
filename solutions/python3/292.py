class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n%4==0 else True