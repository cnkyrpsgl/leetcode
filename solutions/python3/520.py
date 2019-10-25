class Solution:
    def detectCapitalUse(self, word):
        return word[0].isupper() and word[1:].islower() or word.isupper() or word.islower()