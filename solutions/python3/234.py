class Solution:
    def isPalindrome(self, head):
        r = fast = head
        l = None
        while fast and fast.next:
            fast = fast.next.next
            r.next, l, r = l, r, r.next
        if fast: r = r.next
        while l and r and l.val == r.val:
            l, r = l.next, r.next
        return not l