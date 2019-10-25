class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        sim = collections.defaultdict(set)
        for a, b in pairs:
            sim[a].add(b)
            sim[b].add(a)
        return len(words1) == len(words2) and all(w1 == w2 or w2 in sim[w1] for w1, w2 in zip(words1, words2))