class Solution:

    def __init__(self, N, blacklist):
        self.forbidden, self.n, self.used, self.cur = set(blacklist), N, set(), 0
    def pick(self):
        while self.cur in self.forbidden: self.cur += 1
        if self.cur < self.n: num, self.cur = self.cur, self.cur + 1
        else: num = self.used.pop()
        self.used.add(num)
        return num