class Solution:
    def snakesAndLadders(self, board):
        arr, nn, q, seen, moves = [0], len(board) ** 2, [1], set(), 0
        for i, row in enumerate(board[::-1]): arr += row[::-1] if i % 2 else row
        while q:
            new = []
            for sq in q:
                if sq == nn: return moves 
                for i in range(1, 7):
                    if sq + i <= nn and sq + i not in seen:
                        seen.add(sq + i)
                        new.append(sq + i if arr[sq + i] == -1 else arr[sq + i])
            q, moves = new, moves + 1
        return -1                    