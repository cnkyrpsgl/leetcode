class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        cntr, res = collections.Counter(ages), 0
        for A in cntr:
            for B in cntr:
                if B <= 0.5 * A + 7 or B > A: continue
                if A == B: res += cntr[A]  *(cntr[A] - 1)
                else: res += cntr[A] * cntr[B]
        return res