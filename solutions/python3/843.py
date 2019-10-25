# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        n = 0
        while n < 6:
            count = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if sum(i == j for i, j in zip(w1, w2)) == 0)
            guess = min(wordlist, key = lambda w: count[w])
            n = master.guess(guess)
            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(w, guess)) == n]