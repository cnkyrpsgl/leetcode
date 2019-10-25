class Solution:
    def minSteps(self, n):
        cur, copy, steps = 1, 0, 0
        while cur != n:
            if copy < cur and not (n - cur) % cur:
                copy = cur
            else:
                cur += copy
            steps += 1
        return steps