class Solution:
    def combinationSum(self, c, t):
        res, stack, n = [], [(0, [], 0)], len(c)
        while stack:
            sm, tmp, r = stack.pop()
            for i in range(r, n):
                if sm + c[i] < t: 
                    stack.append((sm + c[i], tmp + [c[i]], i))
                elif sm + c[i] == t: 
                    res.append(tmp + [c[i]])
        return res