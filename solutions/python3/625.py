class Solution:
    def smallestFactorization(self, a):
        res = []
        def dfs(num):
            if num == 1: return True
            for n in range(9, 1, -1):
                if not num % n:
                    res.append(str(n))
                    return dfs(num // n)
            return False 
        bol, num = dfs(a), int("".join(sorted(res))) if res else 1
        return num if bol and -(2 ** 31) <= num <= 2 ** 31 - 1 else 0