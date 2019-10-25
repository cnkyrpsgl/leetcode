class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.arr1, self.arr2, self.l1, self.l2 = v1, v2, len(v1), len(v2)
        self.i = self.j = 0
        self.n, self.turn = max(self.l1, self.l2), v1 and 1 or 0

    def next(self):
        if self.turn:
            num = self.arr1[self.i]
            self.i += 1
            if self.j < self.l2:
                self.turn = 0
        else:
            num = self.arr2[self.j]
            self.j += 1
            if self.i < self.l1:
                self.turn = 1
        return num

    def hasNext(self):
        return self.turn and self.i < self.l1 or self.j < self.l2