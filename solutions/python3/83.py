class Solution:
    def deleteDuplicates(self, head):
        cur = root = head
        while head:
            if head.val != cur.val:
                cur.next = cur = head
            head = cur.next = head.next
        return root