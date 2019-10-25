class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.arr = v
        self.rows = len(v)
        self.i = self.j = 0

    def next(self) -> int:
        if self.hasNext():
            self.j += 1
            return self.arr[self.i][self.j - 1]

    def hasNext(self) -> bool:
        if self.arr and self.j == len(self.arr[self.i]):
            self.i += 1
            self.j = 0
        while self.i + 1 < self.rows and not self.arr[self.i]:
            self.i += 1
        return self.i < self.rows and self.arr[self.i] != []
