class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r