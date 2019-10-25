class Solution:
    def findRightInterval(self, intervals):
        def binarySearch(l, r):
            x, found = intervals[l - 1].end, None
            while l <= r:
                mid = (l + r) // 2
                if intervals[mid].start >= x:
                    r = mid - 1
                    found = mid
                else:
                    l = mid + 1
            return ind[intervals[found]] if found != None else -1
        root = intervals[:]
        ind = {intr:i for i, intr in enumerate(root)}
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals)):
            root[ind[intervals[i]]] = binarySearch(i + 1, len(intervals) - 1)
        return root