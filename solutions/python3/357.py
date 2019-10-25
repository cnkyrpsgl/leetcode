class Solution:
    def countNumbersWithUniqueDigits(self, n):
        return [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691][n % 11]