class Solution:
    def findStrobogrammatic(self, n, q = [""]):
        for i in range(n // 2): q = [s + c for s in q  for c in "01689" if i != 0 or c != "0"]
        if n % 2: q = [s + c for s in q for c in "018"]
        for i in range(n // 2 - 1, -1, -1):  q = [s + "9" if s[i] == "6" else s + "6" if s[i] == "9" else s + s[i] for s in q]
        return q