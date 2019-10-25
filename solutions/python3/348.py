class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.rows, self.cols = collections.defaultdict(int), collections.defaultdict(int)
        self.d = self.ad = 0

    def move(self, row, col, player):
        add = player == 1 and 1 or -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.d += add
        if row == self.n - col - 1:
            self.ad += add
        if self.rows[row] == self.n or self.cols[col] == self.n or self.d == self.n or self.ad == self.n:
            return 1
        elif self.rows[row] == -self.n or self.cols[col] == -self.n or self.d == -self.n or self.ad == -self.n:
            return 2
        else:
            return 0