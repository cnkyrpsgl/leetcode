class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        while bits:
            last=bits.pop(0)
            if last==1:bits.pop(0)
        return True if last==0 else False