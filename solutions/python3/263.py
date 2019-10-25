class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>1:
            if num%2!=0 and num%3!=0 and num%5!=0: return False
            else: num/=[i for i in (2,3,5) if num%i==0][-1]
        return num==1