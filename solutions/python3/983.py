class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day, days, last = [0] * 366, set(days), days[-1]
        for i in range(1, last + 1):
            if i not in days:
                day[i] = day[i - 1]
            else:
                day[i] = min(day[i - 1] + costs[0], day[i - 7 if i>= 7 else 0] + costs[1], day[i - 30 if i >= 30 else 0] + costs[2])
        return day[last]