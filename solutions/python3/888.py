class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b = set(A), set(B)
        diff =(sum(A) - sum(B)) // 2
        for c in B:
            if c + diff in a:
                return [c + diff, c]