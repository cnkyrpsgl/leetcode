class LogSystem:

    def __init__(self):
        self.times = []
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}
        
    def put(self, id, timestamp):
        self.times.append([timestamp, id])

    def retrieve(self, s, e, gra):
        ind = self.g[gra]
        s, e = s[:ind], e[:ind]
        return [i for time, i in self.times if s <= time[:ind] <= e]