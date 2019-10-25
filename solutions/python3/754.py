class Solution:
    def reachNumber(self, target):
        pos, step, target = 0, 0, abs(target)
        while pos < target or (pos - target) % 2:
            step += 1
            pos += step
        return step