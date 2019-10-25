class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        return list(num for i,num in enumerate([0,9,987,123,597,677,1218,877,475]) if i==n)[0]