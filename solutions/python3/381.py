class RandomizedCollection:

    def __init__(self):
        self.arr, self.pos = [], collections.defaultdict(set)
    def insert(self, val):
        out = val not in self.pos
        self.arr.append(val)
        self.pos[val].add(len(self.arr) - 1)
        return out

    def remove(self, val):
        if val in self.pos:
            if self.arr[-1] != val:
                x, y = self.pos[val].pop(), self.arr[-1]
                self.pos[y].discard(len(self.arr) - 1)
                self.pos[y].add(x)
                self.arr[x] = y
            else:
                self.pos[val].discard(len(self.arr) - 1)
            self.arr.pop()
            if not self.pos[val]:
                self.pos.pop(val)
            return True 
        return False

    def getRandom(self):
        return random.choice(self.arr)