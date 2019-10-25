class Solution:

    def __init__(self, w):
        self.ranges, sm = [], 0
        for weight in w:
            self.ranges.append([sm, sm + weight])
            sm += weight
        self.mn, self.mx = 1, sm
    def pickIndex(self):
        num, l, r = random.randint(self.mn, self.mx), 0, len(self.ranges) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.ranges[mid][1] < num:
                l = mid + 1
            elif num <= self.ranges[mid][0]:
                r = mid - 1
            else:
                return mid