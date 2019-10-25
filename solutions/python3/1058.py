class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        prices = [float(p) for p in prices]
        sm = sum(math.floor(p) for p in prices)
        prices = sorted(p - math.floor(p) for p in prices if p - math.floor(p))
        if sm > target or target - sm > len(prices):
            return "-1"
        return "{:.3f}".format(sum([p - math.floor(p) for p in  prices[:sm - target]]) + sum([math.ceil(p) - p for p in prices[sm - target:]]))