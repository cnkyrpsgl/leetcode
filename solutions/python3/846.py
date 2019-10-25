class Solution:
    def isNStraightHand(self, hand, W):
        hand.sort()
        while hand:
            try:
                base = hand[0]
                for i in range(W):
                    hand.remove(base+i)
            except:
                return False
        return True