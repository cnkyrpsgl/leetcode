class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l, r, cnt = 0, len(people) - 1, 0
        while l <= r:
            if l != r and people[l] + people[r] > limit: l -= 1
            l += 1
            r -= 1
            cnt += 1
        return cnt