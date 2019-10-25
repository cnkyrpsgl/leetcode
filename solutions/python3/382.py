# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self):
        return random.choice(self.arr)