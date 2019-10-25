class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        words, res, layer = set(wordList), [], {beginWord: [[beginWord]]}
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    for arr in layer[w]:
                        res.append(arr)
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            words -= set(newlayer.keys())
            layer = newlayer
        return res