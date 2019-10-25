class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        return min(sum((c1 - c2) % 2 for c2 in chips) for c1 in chips)