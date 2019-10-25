class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]
        while head:
            arr.append(head)
            head = head.next
        for _ in range(n + 1):
            pre = arr.pop()
        pre.next = pre.next.next
        return dummy.next