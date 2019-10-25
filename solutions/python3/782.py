class Solution:
    def movesToChessboard(self, b):
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)): return -1
        if not N // 2 <= sum(b[0]) <= (N + 1) // 2: return -1
        if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2: return -1
        col = sum(b[0][i] == i % 2 for i in range(N))
        row = sum(b[i][0] == i % 2 for i in range(N))
        if N % 2:
            if col % 2: col = [col, N - col][col % 2]
            if row % 2: row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)
        return (col + row) // 2