class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        q = sorted([[w, u, v] for u, v, w in pipes] + [[w, 0, i+1] for i, w in enumerate(wells)])
        uf = [i for i in range(n+1)]
        res = count = 0
        
        def find(x):
            if (x != uf[x]):
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            uf[x] = y
            
        for w, u, v in q:
            rA, rB = find(u), find(v)
            if rA == rB:
                continue
            union(rA, rB)
            res += w
            count += 1
            if count == n:
                return res
        return res 