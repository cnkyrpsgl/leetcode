class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a, b):
            return a if not b else gcd(b, a % b)
        ab, ac, bc = a * b // gcd(a, b), a * c // gcd(a, c), b * c // gcd(b, c)
        abc = ab * c // gcd(ab, c)
        l, r = 1, 2 * 10 ** 9
        while l < r:
            mid = (l + r) // 2
            if mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc < n:
                l = mid + 1
            else:
                r = mid
        return l
        