# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        intervals = sorted(((intr.start, intr.end) for emp in schedule for intr in emp), key = lambda x: x[0])
        res, stack = [], []
        for s, e in intervals:
            if not stack:
                stack.append((s, e))
            elif s <= stack[-1][-1]:
                stack.append((s, max(e, stack.pop()[1])))
            else:
                res.append([stack[-1][1], s])
                stack.append((s, e))
        return res