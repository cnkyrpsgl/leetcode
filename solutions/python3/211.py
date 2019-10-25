class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.last = False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for char in word:
            if not curr.children[ord(char) - ord("a")]: curr.children[ord(char) - ord("a")] = TrieNode()
            curr = curr.children[ord(char) - ord("a")]
        curr.last = True
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words = [self.root]
        for char in word:
            if char == ".": words = [child for node in words for child in node.children if node and child]
            else: words = [node.children[ord(char) - ord("a")] for node in words if node and node.children[ord(char) - ord("a")]]
        if words and words[-1] == ".": return True
        else: return any([node.last for node in words if node.last])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)