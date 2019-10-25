# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        heap, res, j = [], [], 0
        while head:
            res.append(0)
            while heap and heap[0][0] < head.val:
                val, i = heapq.heappop(heap)
                res[i] = head.val
            heapq.heappush(heap, (head.val, j))
            j += 1
            head = head.next
        return res
        