# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        i = 0
        while i < n:
            person = i
            i += 1
            while i < n and not knows(person, i) and knows(i, person):
                i += 1
        j = person - 1
        while j >= 0 and not knows(person, j) and knows(j, person):
            j -= 1
        return person if j < 0 else -1