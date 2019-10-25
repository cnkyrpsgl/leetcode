class Solution:
    def consecutiveNumbersSum(self, N):
        cnt=0
        for d in range(1, N+1):
            diff=d*(d-1)//2
            nd = N - diff
            if nd<=0: break
            if nd%d==0:
                cnt+=1
        return cnt