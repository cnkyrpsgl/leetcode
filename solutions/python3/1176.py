class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        sm = sum(calories[:k])
        points = (sm > upper) - (sm < lower)
        for i in range(k, len(calories)):
            sm += calories[i] - calories[i - k]
            points += (sm > upper) - (sm < lower)
        return points
            