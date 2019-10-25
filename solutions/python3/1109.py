class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        i = cur = 0
        for j, val in sorted([[i - 1, k] for i, j, k in bookings] + [[j, -k] for i, j, k in bookings]):
            while i < j:
                res[i] = cur
                i += 1
            cur += val
        return res