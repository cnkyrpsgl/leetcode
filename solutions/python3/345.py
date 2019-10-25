class Solution:
    def reverseVowels(self, s):
        r = [c for c in s if c in "aeiouAEIOU"]
        return "".join(c in "aeiouAEIOU" and r.pop() or c for c in s) 