class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2, s3 = [], [], []
        p1, p2 = l1, l2
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        while p2:
            s2.append(p2.val)
            p2 = p2.next
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        residual = 0
        while len(s1) > 0:
            temp = s1.pop() + residual
            if len(s2) > 0:
                temp += s2.pop()
            s3.append(temp % 10)
            residual = temp // 10
        head, p = ListNode(1), l1
        head.next = p
        while len(s3) > 0:
            p.val = s3.pop()
            p = p.next
        return head if residual == 1 else head.next