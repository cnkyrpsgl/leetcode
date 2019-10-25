class Solution:
    def queryString(self, S: str, N: int) -> bool:
        return not set(range(1, N + 1)) - {int(S[i:j + 1], 2) for i in range(len(S)) for j in range(i, len(S))}