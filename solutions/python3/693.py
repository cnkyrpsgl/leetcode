class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a != b for a, b in zip(bin(n)[2:], bin(n)[3:]))
            