class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        for _ in range(len(stones) - 1):
            bisect.insort(stones, stones.pop() - stones.pop())
        return stones[0]