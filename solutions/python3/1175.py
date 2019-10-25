class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        cnt = bisect.bisect(primes, n)
        return math.factorial(cnt) * math.factorial(n - cnt) % (10 ** 9 + 7)
    