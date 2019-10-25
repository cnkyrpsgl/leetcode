class Solution:
    def minEatingSpeed(self, piles, H):
        piles.sort()
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            h = sum(math.ceil(p / mid) for p in piles)
            if h > H:
                l = mid + 1
            elif h < H:
                r = mid - 1
            else:
                return mid
        return l