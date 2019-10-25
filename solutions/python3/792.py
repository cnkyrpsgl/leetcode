class Solution:
    def numMatchingSubseq(self, S, words):
        def check(s, i):
            for c in s:
                i = S.find(c, i) + 1
                if not i: return False
            return True
        return sum((check(word, 0) for word in words))