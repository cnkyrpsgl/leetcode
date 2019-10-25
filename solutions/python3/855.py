class ExamRoom:

    def __init__(self, N):
        self.seated, self.n = [], N - 1
        

    def seat(self):
        if not self.seated:
            self.seated += 0,
            return 0
        mx = ind = 0
        for i in range(1, len(self.seated)):
            l, r = self.seated[i - 1], self.seated[i]
            if (r - l) // 2 > mx:
                mx = (r - l) // 2
                ind = l + mx
        if self.seated[-1] != self.n and self.n - self.seated[-1] > mx:
            mx, ind = self.n - self.seated[-1], self.n
        if self.seated[0] >= mx:
            mx, ind = self.seated[0], 0
        self.seated.append(ind)
        self.seated.sort()
        return ind
        
        
    def leave(self, p):
        self.seated.remove(p)
