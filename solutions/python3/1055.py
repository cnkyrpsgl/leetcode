class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cnt = i = 0
        for t in target:
            i = source.find(t, i)
            if i == -1:
                i = source.find(t, 0)
                if i == -1:
                    return -1
                cnt += 1
            i += 1
        return cnt + 1