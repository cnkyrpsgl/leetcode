class HitCounter(object):

    def __init__(self):
        self.hits = []

    def hit(self, timestamp):
        heapq.heappush(self.hits, timestamp + 300)

    def getHits(self, timestamp):
        while self.hits and self.hits[0] <= timestamp:
            heapq.heappop(self.hits)
        return len(self.hits)