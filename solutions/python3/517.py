class Solution:
    def findMinMoves(self, machines):
        target, n, sm, res, total = sum(machines) // len(machines), len(machines), 0, 0, sum(machines)
        if target * n != total: return -1
        for i in range(n):
            l, sm, r = target * i - sm, sm + machines[i], target * (n - i - 1) - total + sm + machines[i]
            res = max(res, l + r, l, r)
        return res