class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = root = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while root != slow:
                    root = root.next
                    slow = slow.next
                return root
