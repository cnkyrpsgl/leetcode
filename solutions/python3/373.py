class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        n, res, cnt, heap = len(nums2), [], 0, [(nums1[i] + nums2[0], i, 0) for i in range(len(nums1))]
        while heap and cnt < k:
            cnt += 1
            sm, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n: heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res