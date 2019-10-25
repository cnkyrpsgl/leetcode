class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return N > 1 and self.kthGrammar(N - 1, (K + 1) // 2) ^ ((K -1) % 2) or 0