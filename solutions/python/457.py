class Solution(object):
    def circularArrayLoop(self, nums):
        loops, n = [[set(), set()] for _ in range(len(nums))], len(nums)
        for loop in range(3):
            for i, num in enumerate(nums):
                mode = 0 if num > 0 else 1
                if loop == 2 and i in loops[i][mode] and i != (i + num) % n: return True
                loops[(i + num) % n][mode] |= loops[i][mode] or {i}
        return False