class Solution:
    def shortestCompletingWord(self, lp, words):
        cntr_lp, res = {k: v for k, v in collections.Counter(lp.lower()).items() if k.isalpha()}, [None, None]
        for word in words:
            check = collections.Counter(word.lower())
            if all(True if k in check and v <= check[k] else False for k, v in cntr_lp.items()):
                if not any(res) or len(word) < res[1]: res = [word, len(word)]
        return res[0]   