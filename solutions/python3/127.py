class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        words, layer = set(wordList), {beginWord: [[beginWord]]}
        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    return len(layer[w][0])
                else:
                    for i in range(len(w)):
                        for c in string.ascii_lowercase:
                            neww = w[:i] + c + w[i + 1:]
                            if neww in words:
                                newlayer[neww] += [j + [neww] for j in layer[w]]
            words -= set(newlayer.keys())
            layer = newlayer
        return 0