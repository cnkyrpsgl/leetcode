class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def dfs(dr, dc, r, c):
            while 0 <= r <= 7 and 0 <= c <= 7:
                if (r, c) in q:
                    res.append([r, c])
                    break
                r += dr
                c += dc
        q = set((r,c) for r, c in queens)
        res = []
        for dr, dc in (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1):
            dfs(dr, dc, *king)
        return res