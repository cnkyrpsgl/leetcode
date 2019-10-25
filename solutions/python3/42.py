class Solution:
    def trap(self, height):
        res, left, l, r = 0, {}, 0, 0
        for i, h in enumerate(height):
            left[i] = l
            if h > l: 
                l = h
        for i in range(len(height) - 1, -1, -1):
            roof = min(left[i] , r)
            if roof > height[i]:
                res += roof - height[i]
            if height[i] > r:
                r = height[i]
        return res