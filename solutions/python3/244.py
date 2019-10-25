class WordDistance:

    def __init__(self, words):
        self.d = {}
        self.ind = collections.defaultdict(set)
        for i, w in enumerate(words):
            self.ind[w].add(i)
        
    def shortest(self, word1, word2):
        if (word1, word2) not in self.d:
            self.d[(word1, word2)] = self.d[(word2, word1)] = min(abs(j - i) for i in self.ind[word1] for j in self.ind[word2])
        return self.d[(word1, word2)]