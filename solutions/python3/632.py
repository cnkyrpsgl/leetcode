class Solution:
    def smallestRange(self, nums):
        L = R = None
        while True:
            mn = mx = nums[0][-1]
            ind = [0]
            for i, ls in enumerate(nums[1:]):
                if ls[-1] > mx:
                    mx, ind = ls[-1], [i + 1]
                elif ls[-1] == mx:
                    ind.append(i + 1)
                elif ls[-1] < mn:
                    mn = ls[-1]
            if L == None or mx - mn <= R - L:
                L, R = mn, mx
            for j in ind:
                nums[j].pop()
                if not nums[j]:
                    return [L, R]