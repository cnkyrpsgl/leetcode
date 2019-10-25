class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        chain = [r for row in grid for r in row]
        k %= len(chain)
        chain = chain[-k:] + chain[:-k]
        return [chain[i : i + len(grid[0])] for i in range(0, len(chain), len(grid[0]))]

