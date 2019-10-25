class Solution:

    def __init__(self, n_rows, n_cols):
        self.rows, self.cols, self.used = n_rows, n_cols, set()
        
    def flip(self):
        while True:
            r, c = random.randint(1, self.rows), random.randint(1, self.cols)
            if (r, c) not in self.used:
                self.used.add((r, c))
                return [r - 1, c - 1]
            
    def reset(self):
        self.used = set()