class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        for a, b in zip(arr, arr[1:]):
            if b != a + d:
                return a + d
        return 0
        