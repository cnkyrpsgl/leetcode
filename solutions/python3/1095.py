# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l <= r:
            mid = (l  + r) // 2
            md = mountain_arr.get(mid)
            if mid and mountain_arr.get(mid - 1) < md > mountain_arr.get(mid + 1):
                pivot = mid
                break
            elif md < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, pivot
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:
                return mid
            elif md < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = pivot, mountain_arr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            md = mountain_arr.get(mid)
            if md == target:
                return mid
            elif md > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        