class Solution:
    def deckRevealedIncreasing(self, deck):
        ind = list(range(len(deck)))
        for num in sorted(deck):
            deck[ind[0]] = num
            ind = ind[2:] + [ind[1]] if len(ind) > 1 else []
        return deck