# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key = lambda x: x.end); res, curr = 0, -float("inf")
        for i in intervals:
            if curr > i.start: res += 1
            else: curr = i.end
        return res