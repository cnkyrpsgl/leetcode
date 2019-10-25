class Solution:
    def reverseBetween(self, head, m, n):
        dummy_left, dummy_left.next, i = ListNode(0), head, 1
        prev = dummy_left
        while head:
            latter = head.next
            if m == n: 
                break
            if i == m: 
                head_left, right = prev, head
            if i == n: 
                head_right, left = head.next, head
            if m < i <= n: 
                head.next = prev
            prev, head, i = head, latter, i+1
        if m != n: 
            head_left.next, right.next = left, head_right
        return dummy_left.next