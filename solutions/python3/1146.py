class SnapshotArray:

    def __init__(self, length: int):
        self.s = 0
        self.arr = [[[0, 0]] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.s == self.arr[index][-1][0]:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.s, val])

    def snap(self) -> int:
        self.s += 1
        return self.s - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect_left(self.arr[index], [snap_id])
        if i < len(self.arr[index]):
            if self.arr[index][i][0] > snap_id:
                i -= 1
            return self.arr[index][i][1]
        return self.arr[index][-1][1]