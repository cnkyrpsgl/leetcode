class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops==[]:
            return m*n
        return min(op[0] for op in ops)* min(op[1] for op in ops) 