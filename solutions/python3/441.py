class Solution:
    def arrangeCoins(self, n: int) -> int:
        sm = res = 0
        for i in range(1, n + 1):
            sm += i
            if sm > n:
                break
            res += 1
        return res