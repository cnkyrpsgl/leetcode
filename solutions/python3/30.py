class Solution:
    def findSubstring(self, s, words):
        if not s or not words: return []
        cnt, l_words, l_word, cnt_words, res = collections.Counter(words), len(words[0]) * len(words), len(words[0]), len(words), []
        for i in range(len(s) - l_words + 1):
            cur, j = dict(cnt), i
            for _ in range(cnt_words):
                w = s[j:j + l_word]
                if w in cur:
                    if cur[w] == 1: cur.pop(w)
                    else: cur[w] -= 1
                else: break
                j += l_word
            if not cur: res += i,
        return res