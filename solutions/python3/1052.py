class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        dif = mx = sum(c * g for c, g in zip(customers[:x], grumpy[:x]))
        for j in range(x, len(grumpy)):
            dif += (grumpy[j] * customers[j]) - (grumpy[j - x] * customers[j - x])
            mx = max(mx, dif)
        return mx + sum(c * (1- g) for c, g in zip(customers, grumpy))