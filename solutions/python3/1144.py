class Solution:
    def movesToMakeZigzag(self, N: List[int]) -> int:
        moves = [max(0, N[i] - min(N[i-1:i] + N[i+1:i+2]) + 1) for i in range(len(N))]
        return min(sum(moves[::2]), sum(moves[1::2]))