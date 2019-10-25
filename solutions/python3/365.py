class Solution:
    def canMeasureWater(self, x, y, z):
        def gcd(x, y):
            for i in range(min(x, y), -1, -1):
                if not x % i and not y % i: return i      
        div = gcd(x, y) if x * y else 0
        return not z % div and z <= x + y if div else not z