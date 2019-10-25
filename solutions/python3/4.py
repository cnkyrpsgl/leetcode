class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        if len(arr) % 2 == 0: return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
        else: return arr[len(arr) // 2]