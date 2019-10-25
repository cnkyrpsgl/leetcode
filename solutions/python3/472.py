class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        def check(w, st):
            if w in st: return True
            for i in range(1, len(w)):
                if w[:i] in st and check(w[i:], st): return True
            return False
        w_set, res = set(words), []
        for w in words:
            w_set.remove(w)
            if check(w, w_set): res += w,
            w_set.add(w)
        return res