class Solution:
    def findMinDifference(self, tp):
        def getMinute(t): 
            h , m = t.split(":")
            return int(h) * 60 + int(m)
        tp = sorted(map(getMinute, tp))
        mn = sys.maxsize
        for i in range(len(tp) - 1): 
            mn = min(mn, tp[i + 1] - tp[i])
            if mn == 0: return 0
        return min(mn, 1440 + tp[0] - tp[-1])