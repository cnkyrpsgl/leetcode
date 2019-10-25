class Solution:
    def getMoneyAmount(self, n):
        dic = {}
        def dfs(l, r):
            if l >=r: return 0
            if (l, r) not in dic: dic[(l, r)] = min(num + max(dfs(l, num - 1), dfs(num + 1, r)) for num in range(l, r))
            return dic[(l, r)]
        return dfs(1, n)