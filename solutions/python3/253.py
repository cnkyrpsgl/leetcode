# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x: x.start)
        heap, time, rooms = [], 0, 0
        for intr in intervals:
            while heap and heap[0] <= intr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, intr.end)
            if len(heap) > rooms:
                rooms += 1
        return rooms