class Solution:
    def newInteger(self, n):
        base9 = ""
        while n:
            base9 += str(n % 9)
            n //= 9
        return int(base9[::-1])