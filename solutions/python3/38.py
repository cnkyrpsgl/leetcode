class Solution:
    def countAndSay(self, n):
        curr = "1"
        for i in range(n - 1):
            tmp, cnt = "", 1
            for j, c in enumerate(curr):
                if j > 0 and curr[j - 1] == c: 
                    cnt += 1
                elif j > 0: 
                    tmp += str(cnt) + curr[j - 1]
                    cnt = 1
                if j == len(curr) - 1: 
                    tmp += str(cnt) + curr[j] 
            curr = tmp
        return curr