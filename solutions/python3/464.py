class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        memo = {}
        def dfs(arr, total):
            s = str(arr)
            if s in memo:
                return memo[s]
            elif arr[-1] >= total:
                return True
            for i in range(len(arr)):
                if not dfs(arr[:i] + arr[i + 1:], total - arr[i]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)