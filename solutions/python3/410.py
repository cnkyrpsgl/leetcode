class Solution:
    def splitArray(self, nums, m):
        def valid(mid):
            cnt = sm = 0
            for num in nums:
                sm += num
                if sm > mid:
                    cnt += 1
                    if cnt>= m: return False
                    sm = num
            return True
        l, h = max(nums), sum(nums)
        while l < h:
            mid = (l + h) // 2
            if valid(mid):
                h = mid
            else:
                l = mid + 1
        return l