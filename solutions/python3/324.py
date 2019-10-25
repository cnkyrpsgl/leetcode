class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(1, len(nums), 2):
            nums[i] = -heapq.heappop(heap)
        for i in range(0, len(nums), 2):
            nums[i] = -heapq.heappop(heap)