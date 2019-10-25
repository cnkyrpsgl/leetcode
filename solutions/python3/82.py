# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy_left, dummy_left.next = ListNode(0), head
        prev, prev_num = None, dummy_left
        while head:
            if prev and prev.val != head.val: 
                prev_num = prev
            if prev and prev.val == head.val:
                while head and head.next and head.next.val == head.val: 
                    head = head.next
                head = head.next
                prev_num.next = head
            prev = head
            if head: 
                head = head.next
        return dummy_left.next