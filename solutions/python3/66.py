class Solution:
    def plusOne(self, digits, add = 1):
        return add and [1] or [] if not digits else self.plusOne(digits[:-1], +(digits[-1] + add > 9)) + [(digits[-1] + add) % 10]