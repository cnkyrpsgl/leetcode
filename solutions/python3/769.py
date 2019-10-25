class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_seen, total_seen, res_count = 0, 0, 0
        for num in arr:
            max_seen = max(max_seen, num)
            total_seen += 1
            if max_seen == total_seen - 1:
                res_count += 1
        return res_count