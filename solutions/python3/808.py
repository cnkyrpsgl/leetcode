class Solution:
    def soupServings(self, N):
        visited = {}
        def dfs(a, b):
            if (a, b) in visited: return visited[(a, b)]
            elif a <= 0 or b <= 0: return (a < b and 1) or (a == b and 0.5) or (b < a and 0)
            visited[(a, b)] = 0.25 * (dfs(a - 100, b) + dfs(a - 75, b - 25) + dfs(a - 50, b -50) + dfs(a - 25, b - 75))
            return visited[(a, b)] 
        return N > 4800 and 1 or round(dfs(N, N), 5)