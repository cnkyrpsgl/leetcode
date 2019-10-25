# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev, curr = ListNode(None), head
        while curr:
            if curr.val==val:
                if curr==head: head=head.next
                prev.next=curr.next
            if curr.val!=val: prev=curr
            curr=curr.next
        return head