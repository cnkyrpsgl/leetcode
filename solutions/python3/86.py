class Solution:
    def partition(self, head, x):
        lessHead = less = ListNode(-1)
        greatHead = great = ListNode(-1)
        while head:
            if head.val < x:
                less.next = less = head
            else:
                great.next = great = head
            head = head.next
        less.next, great.next = greatHead.next, None
        return lessHead.next