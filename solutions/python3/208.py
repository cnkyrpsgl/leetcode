class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def move(self, word, mod):
        cur = self.root
        for c in word:
            if c not in cur:
                if mod != 1:
                    return False
                cur[c] = {}
            cur = cur[c]
        if mod == 1:
            cur['#'] = None
        else:
            return mod == 3 or '#' in cur
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        return self.move(word, 1)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.move(word, 2)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.move(prefix, 3)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)