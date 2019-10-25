class MyCalendarThree:

    def __init__(self):
        self.times = []

    def book(self, start, end):
        bisect.insort(self.times, (start, 1))
        bisect.insort(self.times, (end, -1))
        res = cur = 0
        for _, x in self.times:
            cur += x
            res = max(res, cur)
        return res