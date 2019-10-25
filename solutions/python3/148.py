# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        ls = []
        while head: ls.append(head.val); head = head.next
        ls .sort()
        root = head = ListNode(ls[0]) if ls else []
        for i in range(1, len(ls)):
            head.next = ListNode(ls[i])
            head = head.next
        return root