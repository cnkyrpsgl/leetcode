class Solution:
    def expressiveWords(self, S, words):
        if not S: return 0
        guide, i, j, res = [], 0, 0, 0
        while i < len(S):
            while j + 1 <len(S) and S[j + 1] == S[j]: j += 1
            guide.append((S[i], j - i + 1))
            i = j = j + 1
        for word in words:
            i = j = g = 0
            while i < len(word):
                while j + 1 < len(word) and word[j + 1] == word[j]: j += 1
                if guide[g][0] != word[i] or (guide[g][1] == 2 and j - i + 1 == 1) or guide[g][1] < j - i + 1: break
                i, j, g = j + 1, j + 1, g + 1
            if g == len(guide): res += 1
        return res