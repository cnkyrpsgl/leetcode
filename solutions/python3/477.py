class Solution:
    def totalHammingDistance(self, nums):
        ones, n, res = [0] * 32, len(nums), 0
        for num in nums:
            for i, c in enumerate(bin(num)[2:][::-1]):
                if c == "1": ones[i] += 1
        for one in ones: res += one * (n - one)
        return res