class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cur = self.root = {}
        self.rank = collections.defaultdict(int)
        for i, s in enumerate(sentences):
            self.s = s
            self.rank[s] = times[i] - 1
            self.input('#')
    
    def move(self, c):
        if c not in self.cur:
            self.cur[c] = {}
        self.cur = self.cur[c]
        if 'sentences' not in self.cur:
            self.cur['sentences'] = []
        
    def addSentence(self):
        self.cur = self.root
        for c in self.s:
            self.move(c)
            self.search()
            heapq.heappush(self.cur['sentences'], [-self.rank[self.s], self.s])
            
    def search(self):
        q, used, i = [], set(), 0
        while i < 3 and self.cur['sentences']:
            r, s = heapq.heappop(self.cur['sentences'])
            if s not in used:
                used.add(s)
                q.append([r, s])
                i += 1
        for r, s in q:
            heapq.heappush(self.cur['sentences'], [r, s])
        return [s for r, s in q]
            
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.rank[self.s] += 1
            self.addSentence()
            self.s = ''
            self.cur = self.root
            return []
        else:
            self.s += c
            self.move(c)
            return self.search()
            


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)