class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.stacks = []
        self.l = [] # pushable
        self.r = [] # poppable
        
    def push(self, val: int) -> None:
        if not self.l:
            # if the rightmost is empty, clear it from self.r
            while self.r and not self.stacks[-self.r[0]]:
                heapq.heappop(self.r)
            i = 0 if not self.r else -self.r[0] + 1
            self.stacks.append([val])
            heapq.heappush(self.r, -i)
            if len(self.stacks[i]) < self.c:
                heapq.heappush(self.l, i)
        else:
            i = self.l[0]
            # new poppable
            if not self.stacks[i]:
                heapq.heappush(self.r, -i)
            self.stacks[i].append(val)
            if len(self.stacks[i]) == self.c:
                heapq.heappop(self.l)
                
    def pop(self) -> int:
        while self.r and not self.stacks[-self.r[0]]:
            heapq.heappop(self.r)
        return self.popAtStack(-self.r[0]) if self.r else -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            ret = self.stacks[index].pop()
            if len(self.stacks[index]) == self.c - 1:
                heapq.heappush(self.l, index)
            return ret
        return -1
        