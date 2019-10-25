class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        prev = None
        for tri in triangle:
            if prev:
                for i, num in enumerate(tri):
                    if i >= len(prev): tri[i] += prev[i - 1]
                    elif i == 0: tri[i] += prev[0]
                    else: tri[i] += min(prev[i - 1], prev[i])
            prev = tri
        return min(triangle[-1])