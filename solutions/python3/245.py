class Solution:
    def shortestWordDistance(self, words, word1, word2):
        i1 = i2 = -1
        res, same = float("inf"), word1 == word2
        for i, w in enumerate(words):
            if w == word1:
                if same: i2 = i1
                i1 = i
                if i2 >= 0: res = min(res, i1 - i2)
            elif w == word2:
                i2 = i
                if i1 >= 0: res = min(res, i2 - i1)
        return res 