class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int("".join([str((int(i)+1)%2) for i in bin(num)[2:]]),2)