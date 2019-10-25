class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        self.m = []

    def addNum(self, num):
        if not self.m:
            self.m = [num]
        elif len(self.m) == 1:
            m = self.m[0]
            if num >= m:
                self.m = [m, heapq.heappushpop(self.r, num)]
            else:
                self.m = [-heapq.heappushpop(self.l, -num), m]
        else:
            m1, m2 = self.m
            if num >= m2:
                heapq.heappush(self.r, num)
                heapq.heappush(self.l, -m1)
                self.m = [m2]
            elif num <= m1:
                heapq.heappush(self.l, -num)
                heapq.heappush(self.r, m2)
                self.m = [m1]
            else:
                heapq.heappush(self.l, -m1)
                heapq.heappush(self.r, m2)
                self.m = [num]

    def findMedian(self):
        return sum(self.m) / len(self.m)