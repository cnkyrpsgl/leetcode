# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def dfs(node):
            if not node.next or dfs(node.next):
                if node.val + 1 > 9:
                    node.val = 0
                    return True
                else:
                    node.val += 1
            return False  
        if dfs(head):
            dummy = ListNode(1)
            dummy.next = head
            return dummy
        return head