# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reorderList(self, head):
        if head:
            arr = []
            while head:
                arr += head,
                head = head.next
            l, r, prev = 0, len(arr) - 1, ListNode(0)
            while l < r: prev.next, arr[l].next, prev, l, r = arr[l], arr[r], arr[r], l + 1, r - 1
            if l == r: prev.next = arr[l]
            arr[l].next = None