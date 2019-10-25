class Solution:
    def validWordSquare(self, words):
        for j, row in enumerate(words):
            col = ""
            for s in words:
                try: col += s[j]
                except: break
            if row != col: return False
        return True