class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sm, div =1, 2
        while div**2<=num:
            if num%div==0: sm+=div+(num//div)
            div+=1
        return sm==num and div>2