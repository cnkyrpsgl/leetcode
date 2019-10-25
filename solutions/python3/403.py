class Solution:
    def canCross(self, stones):
        memo, stones, target = {}, set(stones), stones[-1]
        def dfs(unit, last):
            if unit == target: return True
            if (unit, last) not in memo: 
                memo[(unit, last)] = any(dfs(unit + move, move) for move in (last - 1, last, last + 1) if move and unit + move in stones)
            return memo[(unit, last)]
        return dfs(1, 1) if 1 in stones else False