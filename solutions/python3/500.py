class Solution:
    def findWords(self, words):
        return [w for w in words if any(not set(w.lower()) - row for row in (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")))]