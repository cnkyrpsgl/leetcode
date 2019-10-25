class Solution:
    def calculateTime(self, k: str, word: str) -> int:
        return sum(abs(k.index(a) - k.index(b)) for a, b in zip(k[0] + word, word))