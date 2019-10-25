class Solution:
    def findKthNumber(self, n, k):
        def calSteps(n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps
        cur = 1
        k -= 1
        while k:
            steps = calSteps(cur, cur + 1)
            if steps <= k:
                cur += 1
                k -= steps
            else:
                cur *= 10
                k -= 1
        return cur