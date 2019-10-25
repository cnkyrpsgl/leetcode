class Solution:
    def maxArea(self, height):
        left, right, mx = 0, len(height) - 1, 0
        while left < right:
            mx = max(mx, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return mx