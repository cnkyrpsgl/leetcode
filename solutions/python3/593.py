class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        from itertools import combinations as cb
        def D(C): 
            return (C[0][0] - C[1][0]) ** 2 + (C[0][1] - C[1][1]) ** 2
        S = set(map(D, cb((p1, p2, p3, p4), 2)))
        return len(S) == 2 and 0 not in S