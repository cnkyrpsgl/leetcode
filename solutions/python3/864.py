class Solution:
    def shortestPathAllKeys(self, grid):
        final, m, n, si, sj = 0, len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    final |= 1 << ord(grid[i][j]) - ord("a")
                elif grid[i][j] == "@":
                    si, sj = i, j
        q, memo = [(0, si, sj, 0)], set()
        while q:
            moves, i, j, state = heapq.heappop(q)
            if state == final: return moves
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != "#":
                    if grid[x][y].isupper() and not state & 1 << (ord(grid[x][y].lower()) - ord("a")): continue
                    newState = ord(grid[x][y]) >= ord("a") and state | 1 << (ord(grid[x][y]) - ord("a")) or state
                    if (newState, x, y) not in memo:
                        memo.add((newState, x, y))
                        heapq.heappush(q, (moves + 1, x, y, newState))
        return -1