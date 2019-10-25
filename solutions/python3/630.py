class Solution:
    def scheduleCourse(self, courses):
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda x: x[1]):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)