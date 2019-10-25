class Solution:
    def dayOfYear(self, date: str) -> int:
        cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        y, m, d = map(int, date.split('-'))
        days = sum(cnt[:m - 1]) + d
        if m > 2:
            if y % 400 == 0: days += 1
            if y % 100 == 0: return days
            if y % 4 == 0: days += 1
        return days