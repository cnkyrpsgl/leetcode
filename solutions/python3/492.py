class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        l, w = int(math.sqrt(area)), int(math.sqrt(area))
        while l*w!=area:
            if area%w==0: l=int(area/w)
            else: w-=1
        return [l,w]