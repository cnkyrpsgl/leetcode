class Solution:
    def findIntegers(self, num):
        num, sub = bin(num)[2:], 0
        zero, one = [1] * len(num), [1] * len(num)
        for i in range(1, len(num)):
            zero[i], one[i] = zero[i - 1] + one[i - 1], zero[i - 1]
        for i in range(1, len(num)):
            if num[i] == num[i - 1] == "1": break
            if num[i] == num[i - 1] == "0": sub += one[-1 - i]
        return zero[-1] + one[-1] - sub