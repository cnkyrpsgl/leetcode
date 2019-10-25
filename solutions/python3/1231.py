class Solution:
    def maximizeSweetness(self, sw: List[int], K: int) -> int:
        def ok(m):
            c = sm = 0
            for s in sw:
                sm += s
                if sm >= m:
                    sm = 0 
                    c += 1
            return c >= K + 1
        l, r = 1, sum(sw)
        while l < r:
            m = (l + r) // 2
            if ok(m):
                l = m + 1
            else:
                r = m - 1
        print(l, r)
        return r if ok(r) else l - 1
        