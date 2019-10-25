class Solution:
    def shortestDistance(self, words, word1, word2):
        i1, i2, mn = -1, -1, float("inf")
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
                if i2 >= 0:
                    mn = min(mn, i - i2)
            elif w == word2:
                i2 = i
                if i1 >= 0:
                    mn = min(mn, i - i1)
        return mn