from functools import reduce


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(math.gcd, nums) == 1
