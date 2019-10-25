class Solution:
    def maxProduct(self, words):
        sets, mx = {w: set(w) for w in words}, 0
        words.sort(key = len, reverse = True)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= mx:
                    break
                elif not sets[words[i]] & sets[words[j]]:
                    mx = len(words[i]) * len(words[j])
        return mx