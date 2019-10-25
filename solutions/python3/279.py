class Solution:
    def numSquares(self, n):
        q, move = {i ** 2 for i in range(1, int(n ** 0.5) + 1)}, 1
        coins = set(q)
        while q:
            if n in q: return move
            q = {sm + c for sm in q for c in coins} - q
            move += 1