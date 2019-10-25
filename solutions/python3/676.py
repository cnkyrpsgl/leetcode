class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.var = defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for w in dict:
            for i in range(len(w)): self.var[(i, w[:i] + w[i + 1:])].add(w[i])
    
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in range(len(word)): 
            if self.var[(i, word[:i] + word[i + 1:])] - {word[i]}: return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)