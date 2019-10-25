class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new, i = [], 0
        for i, it in enumerate(intervals):
            if newInterval[1] < it[0]: 
                i -= 1
                break
            elif it[1] < newInterval[0]: 
                new += it,
            else: 
                newInterval[0], newInterval[1] = min(it[0], newInterval[0]), max(it[1], newInterval[1])
        return new + [newInterval] + intervals[i + 1:]
        