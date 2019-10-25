class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                adj = [M[i + x][j + y] for x, y in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)) if 0 <= i + x < m and 0 <= j + y < n] 
                grid[i][j] = sum(adj) // len(adj)
        return grid
                    
        