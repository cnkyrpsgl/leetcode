class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        s = set(words)
        for word in words: 
            for i in range(1, len(word)): s.discard(word[i:])
        return sum(len(w) + 1 for w in s)