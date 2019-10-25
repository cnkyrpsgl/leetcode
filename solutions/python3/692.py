class Solution:
    def topKFrequent(self, words, k):
        return [w for w, v in sorted(collections.Counter(words).items(), key = lambda x: (-x[1], x[0])) [:k]]