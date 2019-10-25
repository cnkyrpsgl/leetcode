# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key = lambda x: x.end)
        for intr in intervals:
            if not re:
                res.append([intr.start, intr.end])
            else:
                s = intr.start
                while res and res[-1][1] >= intr.start:
                    s = min(s, res.pop()[0])
                res.append([s, intr.end])
        return res