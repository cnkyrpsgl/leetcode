# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        q = []
        for i in range(len(lists)):
            while lists[i]:
                q += lists[i],
                lists[i] = lists[i].next
        root = cur = ListNode(0)
        for h in sorted(q, key = lambda x: x.val):
            cur.next = cur = h
        return root.next