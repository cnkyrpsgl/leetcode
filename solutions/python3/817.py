# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        num_connected = 0
        set_g = set(G)
        while head:
            if head.val not in set_g:
                head = head.next
                continue
            while head and head.val in set_g:
                head = head.next
            num_connected += 1
        return num_connected