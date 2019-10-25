class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            mp12, mp21, match = {}, {}, True
            for c1, c2 in zip(w, pattern):
                if (c1 in mp12 and mp12[c1] != c2) or (c2 in mp21 and mp21[c2] != c1):
                    match = False
                    break
                mp12[c1], mp21[c2] = c2, c1
            if match: res.append(w)
        return res