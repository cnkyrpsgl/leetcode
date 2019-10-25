class Solution:
    def maxNumber(self, nums1, nums2, k):
        def merge(arr1, arr2):
            res, i, j = [], 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i:] >= arr2[j:]:
                    res.append(arr1[i])
                    i += 1
                else: 
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1): res += arr1[i:]
            elif j < len(arr2): res += arr2[j:]
            return res     
        
        def makeArr(arr, l):
            i, res = 0, []
            for r in range(l - 1, -1, -1):
                num, i = max(arr[i:-r] or arr[i:])
                i = -i + 1
                res.append(num)
            return res
        
        nums1, nums2, choices = [(num, -i) for i, num in enumerate(nums1)], [(num, -i) for i, num in enumerate(nums2)], []
        for m in range(k + 1):
            if m > len(nums1) or k - m > len(nums2): continue
            arr1, arr2 = makeArr(nums1, m), makeArr(nums2, k - m)  
            choices.append(merge(arr1, arr2))
        return max(choices)
            