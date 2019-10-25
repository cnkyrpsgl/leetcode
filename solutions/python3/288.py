class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.pool = collections.defaultdict(set)
        for w in dictionary:
            self.pool[w[2:] and w[0] + str(len(w) - 2) + w[-1] or w].add(w)
            

    def isUnique(self, w: str) -> bool:
        return not self.pool[w[2:] and w[0] + str(len(w) - 2) + w[-1] or w] - {w}


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)