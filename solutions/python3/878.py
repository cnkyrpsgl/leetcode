class Solution:
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def count(self, num, A, B, C):
        return num // A + num // B - num // C
    
    def nthMagicalNumber(self, N, A, B):
        l, r, C = 2, 2 ** 63  - 1, A * B // self.gcd(A, B)
        while l < r:
            mid = (l + r) // 2
            if self.count(mid, A, B, C) < N:
                l = mid + 1
            else:
                r = mid
        return l % (10 ** 9 + 7)