class SummaryRanges:

    def __init__(self):
        self.starts, self.ends, self.used = [-float("inf"), float("inf")], [-float("inf"), float("inf")], set()
        
    def addNum(self, val):
        if val not in self.used:
            self.used.add(val)
            i = bisect.bisect_left(self.starts, val) - 1
            if self.ends[i] + 1 == val and val + 1 == self.starts[i + 1]: # if val is the gap btw 2 intervals
                del self.starts[i + 1]
                del self.ends[i]
            elif self.ends[i] + 1 == val: #if val is adjacent to current end
                self.ends[i] += 1
            elif self.starts[i + 1] == val + 1: # if val is adjacent to next start
                self.starts[i + 1] -= 1
            elif val > self.ends[i]: # if val is independent of those 2 intervals
                self.starts.insert(i + 1, val) 
                self.ends.insert(i + 1, val)
            
    def getIntervals(self):
        return [[s, e] for s, e in zip(self.starts[1:-1], self.ends[1:-1])] #exclude infinity