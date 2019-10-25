class Solution:
    def findTheDifference(self, s, t):
        return next(iter(collections.Counter(t) - collections.Counter(s)))