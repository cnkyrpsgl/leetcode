class Solution:
    def findContestMatch(self, n):
        arr = [str(i) for i in range(1, n + 1)]
        while len(arr) > 1: arr = ["(" + arr[i] + "," + arr[len(arr) - 1 - i] + ")" for i in range(len(arr) // 2)]
        return ",".join(arr)    