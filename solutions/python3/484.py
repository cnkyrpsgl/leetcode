class Solution:
    def findPermutation(self, s):
        arr, cnt, n = list(range(1, len(s) + 2)), 0, len(s)
        for i in range(n + 1):
            if i < n and s[i] == "D":
                cnt += 1
            elif cnt:
                arr[i - cnt:i + 1] =  arr[i - cnt:i + 1][::-1]
                cnt = 0
        return arr