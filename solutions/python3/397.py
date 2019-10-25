class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: 
            return 0
        elif n % 2 == 0: 
            return self.integerReplacement(n/2)+1
        else: 
            return min(self.integerReplacement(n+1),self.integerReplacement(n-1))+1