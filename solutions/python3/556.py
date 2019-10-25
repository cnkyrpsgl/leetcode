class Solution:
    def nextGreaterElement(self, n):
        arr = [c for c in str(n)]
        for l in range(len(arr) - 2, -1, -1):
            r = len(arr) - 1
            while l < r and arr[r] <= arr[l]:
                r -= 1
            if l != r:
                arr[l], arr[r] = arr[r], arr[l]
                arr[l + 1:] = sorted(arr[l + 1:])
                num = int("".join(arr))
                return num if -2 ** 31 <= num <= 2 ** 31 - 1 else -1
        return -1