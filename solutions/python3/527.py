class Solution:
    def wordsAbbreviation(self, dict):
        abb = collections.defaultdict(int)
        for i, w in enumerate(dict):
            for j in range(1, len(w) - 2):
                abb[w[:j] + str(len(w) - j - 1) + w[-1]] += 1
        for i, w in enumerate(dict):
            for j in range(1, len(w) - 2):
                new = w[:j] + str(len(w) - j - 1) + w[-1]
                if abb[new] == 1:
                    dict[i] = new
                    break
        return dict