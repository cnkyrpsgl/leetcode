class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]))
        a = b = 0
        N = len(costs) // 2
        c = 0
        for c1, c2 in costs[::-1]:
            if c1 <= c2 and a < N or b >= N:
                c += c1
                a += 1
            else:
                c += c2
                b += 1
        return c