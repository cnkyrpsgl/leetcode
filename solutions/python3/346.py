class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.arr = collections.deque(maxlen = size)

    def next(self, val: int) -> float:
        self.arr.append(val)
        return sum(self.arr) / len(self.arr)
        
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)