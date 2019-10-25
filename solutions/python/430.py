class Solution(object):
    def flatten(self, head):
        stack, cur, root = [], head, head
        while stack or cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                new = cur.child
                new.prev = cur
                cur.child = None
                cur.next = cur = new
            elif not cur.next and stack:
                cur.next = stack.pop()
                cur.next.prev = cur
                cur = cur.next
            else:
                cur = cur.next
        return root