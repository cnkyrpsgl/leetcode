class Solution:
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()[::-1]
        return '-'.join([S[i:i+K] for i in range(0, len(S), K)])[::-1]