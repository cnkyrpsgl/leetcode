class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "T":
                    tX, tY = r, c
                if grid[r][c] == "B":
                    bX, bY = r, c
                if grid[r][c] == "S":
                    pX, pY = r, c

        def heuristic(bX, bY):
            return abs(tX - bX) + abs(tY - bY)

        heap = [[heuristic(bX, bY), 0, pX, pY, bX, bY]]
        visited = set()
        while heap:
            _, moves, pX, pY, bX, bY = heapq.heappop(heap)
            if bX == tX and bY == tY:
                return moves
            if (pX, pY, bX, bY) not in visited:
                visited.add((pX, pY, bX, bY))
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    pX += dx
                    pY += dy
                    if 0 <= pX < m and 0 <= pY < n and grid[pX][pY] != "#":
                        if pX == bX and pY == bY:
                            bX += dx
                            bY += dy
                            if 0 <= bX < m and 0 <= bY < n and grid[bX][bY] != "#":
                                heapq.heappush(
                                    heap,
                                    [
                                        heuristic(bX, bY) + moves + 1,
                                        moves + 1,
                                        pX,
                                        pY,
                                        bX,
                                        bY,
                                    ],
                                )
                            bX -= dx
                            bY -= dy
                        else:
                            heapq.heappush(
                                heap, [heuristic(bX, bY) + moves, moves, pX, pY, bX, bY]
                            )
                    pX -= dx
                    pY -= dy
        return -1
