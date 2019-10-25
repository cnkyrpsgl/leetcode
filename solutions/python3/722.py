class Solution:
    def removeComments(self, source):
        res, block, cont, blockStart = [], False, False, -1
        for line in source:
            if not cont: cache = ""
            for i, c in enumerate(line):
                if not block: cache += c
                if cache[-2:] == "//":
                    cache = cache[:-2]
                    break
                elif cache[-2:] == "/*": blockStart, cache, block = i, cache[:-2], True
                elif line[i - 1:i + 1] == "*/" and blockStart < i - 1: block = False
            if not block:
                if cache: res += cache,
                cont = False
            else: cont, blockStart = True, -1
        return res