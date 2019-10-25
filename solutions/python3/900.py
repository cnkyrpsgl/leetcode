class RLEIterator:

    def __init__(self, A):
        self.it = A[::-1]

    def next(self, n):
        while self.it and self.it[-1] <= n:
            if self.it[-1]: last = self.it[-2]
            n -= self.it.pop()
            self.it.pop()
        if n and self.it:
            self.it[-1] -= n
            last = self.it[-2]
        return last if self.it else -1
        