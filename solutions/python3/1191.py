class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int, mod = 10 ** 9 + 7) -> int:
        def Kadane(arr, res = 0, cur = 0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res
        return ((k - 2) * max(sum(arr), 0) + Kadane(arr * 2) ) % mod if k > 1 else Kadane(arr) % mod