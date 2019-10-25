class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in sorted(words, key = lambda x: (-len(x), x)):
            if all([True if w[:i] in set(words) - {w} else False for i in range(1, len(w))]): return w  
        return ""