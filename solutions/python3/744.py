class Solution:
    def nextGreatestLetter(self, letters, target):
        return letters[bisect.bisect(letters, target) % len(letters)]