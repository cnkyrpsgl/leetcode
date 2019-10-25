class Solution:
    def bitwiseComplement(self, N: int, M = 0, m = 0) -> int:
        return N ^ M if M and M >= N else self.bitwiseComplement(N, M + 2 ** m, m + 1)