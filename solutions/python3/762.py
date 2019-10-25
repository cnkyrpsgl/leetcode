class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count=0
        while L<=R:
            if str(bin(L)[2:]).count("1") in [2,3,5,7,11,13,17,19]: count+=1
            if str(bin(R)[2:]).count("1") in [2,3,5,7,11,13,17,19]:
                count+=1
                if L==R: count-=1
            L+=1
            R-=1
        return count