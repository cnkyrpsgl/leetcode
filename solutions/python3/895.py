class FreqStack:

    def __init__(self):
        self.stacks = collections.defaultdict(list)
        self.freq = collections.Counter()
        self.maxFreq = 0

    def push(self, x):
        self.freq[x] += 1 
        self.maxFreq = max(self.maxFreq, self.freq[x])
        self.stacks[self.freq[x]].append(x)

    def pop(self):
        num = self.stacks[self.maxFreq].pop()
        self.freq[num] -= 1 
        if not self.stacks[self.maxFreq]: self.maxFreq -= 1
        return num