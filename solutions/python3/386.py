class Solution:
    def lexicalOrder(self, n): return sorted(range(1, n + 1), key = str)