class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        def dfs(i, mod, cnt):
            res[i][mod] = cnt
            for v in edge[i][mod]:
                if cnt < res[v][1 - mod]:
                    dfs(v, 1 - mod, cnt + 1)
                    
        res = [[float('inf'), float('inf')] for _ in range(n)]
        edge = [[[], []] for _ in range(n)]
        for u, v in red_edges:
            edge[u][0].append(v)
        for u, v in blue_edges:
            edge[u][1].append(v)
        dfs(0, 0, 0)
        dfs(0, 1, 0)
        return [x if x != float('inf') else -1 for x in map(min, res)]