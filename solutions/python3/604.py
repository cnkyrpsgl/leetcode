class StringIterator:
    def findCount(self):
        j = self.ind + 1
        while j < self.n and self.s[j].isnumeric(): j += 1
        self.count = int(self.s[self.ind + 1:j])
        self.new = j
        
    def __init__(self, compressedString):
        self.s, self.n = compressedString, len(compressedString)
        self.ind = self.count = self.new = 0
        self.findCount()

    def next(self):
        if not self.count:
            if self.new >= self.n: return " "
            elif self.new < self.n:
                self.ind = self.new
                self.findCount()
        self.count -= 1
        return self.s[self.ind]

    def hasNext(self):
        return self.count > 0 or self.new < self.n - 1