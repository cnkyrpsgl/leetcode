class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head.next if head else None
        while slow != None and fast != None:
            if slow == fast:
                return True
            slow, fast = slow.next, fast.next.next if fast.next else None
        return False
