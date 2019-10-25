class Solution:
    def nextClosestTime(self, time):
        t = sorted(set(time))[:-1]  
        nex = {a: b for a, b in zip(t, t[1:])}
        for i, d in enumerate(time[::-1]):
            if d in nex:
                if i == 0:
                    return time[:4] + nex[d]
                elif i == 1 and nex[d] < '6':
                    return time[:3] + nex[d] + t[0]
                elif i == 3 and int(time[0] + nex[d]) < 24:
                    return time[0] + nex[d] + ':' + t[0] * 2
        return t[0] * 2 + ':' + t[0] * 2