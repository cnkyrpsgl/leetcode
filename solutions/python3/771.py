class Solution:
    def numJewelsInStones(self, J, S):
        sj = set(J)
        return sum(s in sj for s in S)