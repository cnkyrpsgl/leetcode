class Solution(object):
    def getIntersectionNode(self, headA, headB):
        r1, r2, l1, l2 = headA, headB, 0, 0
        while headA: headA, l1 = headA.next, l1 + 1
        while headB: headB, l2 = headB.next, l2 + 1
        while l1 > l2: r1, l1 = r1.next, l1 - 1
        while l2 > l1: r2, l2 = r2.next, l2 - 1
        while r1 != r2: r1, r2 = r1.next, r2.next
        return r1