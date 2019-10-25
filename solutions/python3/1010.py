class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 61
        for t in time:
            mod[-1] += mod[(60 - t % 60) % 60]
            mod[t % 60] += 1
        return mod[-1]